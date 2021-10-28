-- ** Cleaning Data in SQL Queries **


SELECT *
FROM [Portfolio Project 2 Housing]..[Nashville Housing]


-- Standardize Date Format

SELECT SaleDate, CONVERT(DATE, SaleDate)
FROM [Portfolio Project 2 Housing]..[Nashville Housing]

UPDATE [Nashville Housing]
SET SaleDate = CONVERT(DATE, SaleDate)

ALTER TABLE [Nashville Housing]
ADD SaleDateConverted DATE;

UPDATE [Nashville Housing]
SET SaleDateConverted = CONVERT(DATE, SaleDate)

SELECT SaleDateConverted, CONVERT(DATE, SaleDate)
FROM [Portfolio Project 2 Housing]..[Nashville Housing]

 
 -- Populate Property Address data
 
SELECT *
FROM [Portfolio Project 2 Housing]..[Nashville Housing]
ORDER BY ParcelID


--Populate missing PropertyAddress by matching to ParcelID

SELECT a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ISNULL (a.PropertyAddress, b.PropertyAddress)
FROM [Portfolio Project 2 Housing]..[Nashville Housing] AS a
JOIN [Portfolio Project 2 Housing]..[Nashville Housing] AS b
	ON a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID ]
WHERE a.PropertyAddress IS NULL

UPDATE a
SET PropertyAddress = ISNULL (a.PropertyAddress, b.PropertyAddress)
FROM [Portfolio Project 2 Housing]..[Nashville Housing] AS a
JOIN [Portfolio Project 2 Housing]..[Nashville Housing] AS b
	ON a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID ]
WHERE a.PropertyAddress IS NULL


-- Breaking out Address into Individual Columns (Address, City, State)

SELECT PropertyAddress
FROM [Portfolio Project 2 Housing]..[Nashville Housing]


SELECT
SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1) AS Address
, SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) +1, LEN(PropertyAddress)) AS City --Change second Address to City?
FROM [Portfolio Project 2 Housing]..[Nashville Housing]


ALTER TABLE [Nashville Housing]
ADD PropertySplitAddress NVarChar(255);

UPDATE [Nashville Housing]
SET PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1)


ALTER TABLE [Nashville Housing]
ADD PropertySplitCity NVarChar(255);

UPDATE [Nashville Housing]
SET PropertySplitCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) +1, LEN(PropertyAddress))


--And again for OwnerAddress

SELECT OwnerAddress
FROM [Portfolio Project 2 Housing]..[Nashville Housing]


SELECT
PARSENAME(REPLACE(OwnerAddress, ',', '.') ,3)
, PARSENAME(REPLACE(OwnerAddress, ',', '.') ,2)
, PARSENAME(REPLACE(OwnerAddress, ',', '.') ,1)
FROM [Portfolio Project 2 Housing]..[Nashville Housing]


ALTER TABLE [Nashville Housing]
ADD OwnerSplitAddress NVarChar(255);

UPDATE [Nashville Housing]
SET OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',', '.') ,3)


ALTER TABLE [Nashville Housing]
ADD OwnerSplitCity NVarChar(255);

UPDATE [Nashville Housing]
SET OwnerSplitCity = PARSENAME(REPLACE(OwnerAddress, ',', '.') ,2)


ALTER TABLE [Nashville Housing]
ADD OwnerSplitState NVarChar(255);

UPDATE [Nashville Housing]
SET OwnerSplitState = PARSENAME(REPLACE(OwnerAddress, ',', '.') ,1)


-- Change Y and N to Yes and No in "Sold as Vacant" field

SELECT DISTINCT(SoldAsVacant), COUNT(SoldAsVacant)
FROM [Portfolio Project 2 Housing]..[Nashville Housing]
GROUP BY SoldAsVacant
ORDER BY 2


SELECT SoldAsVacant
, CASE WHEN SoldAsVacant = 'Y' THEN 'Yes'
	WHEN SoldAsVacant = 'n' THEN 'No'
	ELSE SoldAsVacant
	END
FROM [Portfolio Project 2 Housing]..[Nashville Housing]

UPDATE [Nashville Housing]
SET SoldAsVacant = CASE WHEN SoldAsVacant = 'Y' THEN 'Yes'
	WHEN SoldAsVacant = 'n' THEN 'No'
	ELSE SoldAsVacant
	END


-- Remove Duplicates (NOT standard practice to do this)

WITH RowNumCTE AS (
SELECT *,
	ROW_NUMBER() OVER (
	PARTITION BY ParcelID, 
				PropertyAddress,
				SalePrice,
				SaleDate,
				LegalReference
				ORDER BY
					UniqueID
					) RowNum

FROM [Portfolio Project 2 Housing]..[Nashville Housing]
)

DELETE
FROM RowNumCTE
WHERE RowNum > 1


-- Delete Unused Columns

SELECT *
FROM [Portfolio Project 2 Housing]..[Nashville Housing]


ALTER TABLE [Portfolio Project 2 Housing]..[Nashville Housing]
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress, SaleDate

ALTER TABLE [Portfolio Project 2 Housing]..[Nashville Housing]
DROP COLUMN SaleDate
