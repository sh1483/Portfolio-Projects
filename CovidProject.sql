--SELECT *
--FROM PortfolioProject..CovidDeaths
--ORDER BY 3,4

--SELECT *
--FROM PortfolioProject..CovidVaccinations
--ORDER BY 3,4

--Select Data that we are going to be using

SELECT Location, date, total_cases, new_cases, total_deaths, population
FROM PortfolioProject..CovidDeaths
ORDER BY 1,2


-- Looking at Total Cases vs Total Deaths in the USA
--Shows chances of dying if you contract COVID in the USA

SELECT Location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 AS DeathPercentage
FROM PortfolioProject..CovidDeaths
WHERE location LIKE '%states%'
ORDER BY 1,2

--Looking at Total Cases VS Population
--Shows percentage of population that contracted COVID

SELECT Location, date, total_cases, (total_cases/population)*100 AS InfectionPercentage
FROM PortfolioProject..CovidDeaths
WHERE continent IS NOT Null
ORDER BY 1,2


--Looking at countries with highest infection rate compared to population

SELECT Location, population, MAX(total_cases) AS MostInfections, MAX((total_cases/population))*100 AS InfectionPercentage
FROM PortfolioProject..CovidDeaths
WHERE continent IS NOT Null
GROUP BY Location, population
ORDER BY 4 DESC


--Shows countries with highest death count

SELECT Location, MAX(CAST(total_deaths AS INT)) AS MostDeaths
FROM PortfolioProject..CovidDeaths
WHERE continent IS NOT Null
GROUP BY Location
ORDER BY 2 DESC


--Shows countries with highest death count PER POPULATION

SELECT Location, population, MAX(CAST(total_deaths AS INT)/population)*100 AS MostDeaths
FROM PortfolioProject..CovidDeaths
WHERE continent IS NOT Null
GROUP BY Location, population
ORDER BY 3 DESC


--Shows worldwide and continent death count

SELECT location, MAX(CAST(total_deaths AS INT)) AS MostDeaths
FROM PortfolioProject..CovidDeaths
WHERE continent IS Null
GROUP BY location
ORDER BY 2 DESC


--Shows continents with highest death count

SELECT continent, MAX(CAST(total_deaths AS INT)) AS MostDeaths
FROM PortfolioProject..CovidDeaths
WHERE continent IS NOT Null
GROUP BY continent
ORDER BY 2 DESC


--Global Numbers

SELECT SUM(new_cases) AS total_cases, SUM(CAST(new_deaths AS INT)) AS total_deaths, SUM(CAST(new_deaths AS INT))/SUM(new_cases)*100 AS DeathPercentage
FROM PortfolioProject..CovidDeaths
WHERE continent IS NOT Null
ORDER BY 1,2


--Joined Tables

-- Looking at Total Population vs Vaccinations

SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(INT,vac.new_vaccinations)) OVER (PARTITION BY dea.location ORDER BY dea.location,
	dea.date) AS RollingVaccinationCount
FROM PortfolioProject..CovidDeaths AS dea
JOIN PortfolioProject..CovidVaccinations AS vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent IS NOT Null
ORDER BY 2,3



--USE CTE

WITH PopvsVAC (Continent, Location, Date, Population, New_Vaccination, RollingVaccinationCount)
AS
(
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(INT,vac.new_vaccinations)) OVER (PARTITION BY dea.location ORDER BY dea.location,
	dea.date) AS RollingVaccinationCount
--	, (RollingVaccinationCount/population)*100
FROM PortfolioProject..CovidDeaths AS dea
JOIN PortfolioProject..CovidVaccinations AS vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent IS NOT Null
--ORDER BY 2,3
)
SELECT *, (RollingVaccinationCount/Population)*100 AS PercentVaccinated
FROM PopvsVAC


-- TEMP TABLE (Not working for some reason)

DROP TABLE IF EXISTS #PercentPopulationVaccinated
CREATE TABLE #PercentPopulationVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
DATE datetime,
Population numeric,
New_Vaccinations numeric,
RollingVaccinationCount numeric
)

INSERT INTO #PercentPopulationVaccinated
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(INT,vac.new_vaccinations)) OVER (PARTITION BY dea.location ORDER BY dea.location,
	dea.date) AS RollingVaccinationCount
--	, (RollingVaccinationCount/population)*100
FROM PortfolioProject..CovidDeaths AS dea
JOIN PortfolioProject..CovidVaccinations AS vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent IS NOT Null
--ORDER BY 2,3

SELECT *, (RollingVaccinationCount/Population)*100
FROM #PercentPopulationVaccinated




-- Creating View to store data for later visualizations (NOT WORKING)

CREATE VIEW RollingVacCount AS

SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(INT,vac.new_vaccinations)) OVER (Partition by dea.Location
	Order by dea.location, dea.Date) AS RollingVaccinationCount
--, (RollingVaccinationCount/population)*100
FROM PortfolioProject..CovidDeaths AS dea
JOIN PortfolioProject..CovidVaccinations AS vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent is not null

SELECT *
FROM RollingVacCount

