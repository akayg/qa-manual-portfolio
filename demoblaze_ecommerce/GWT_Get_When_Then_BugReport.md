**Test Case ID**: TC_001  
**Title**: Verify homepage title

**Given** the user has internet access and browser is open  
**When** the user navigates to https://www.demoblaze.com  
**Then** the page title should be “STORE”



**Test Case ID**: TC_002  
**Title**: Verify user can click on 'Laptops' category

**Given** the user is on the homepage of DemoBlaze  
**When** the user clicks on the “Laptops” category on the sidebar  
**Then** a list of laptop products should be displayed


**Test Case ID**: TC_003  
**Title**: Verify Add to Cart functionality

**Given** the user is on the product listing page  
**When** the user clicks on a product and then clicks "Add to Cart"  
**Then** a confirmation popup should appear saying “Product added”
