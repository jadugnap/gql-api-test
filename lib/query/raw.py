# lib/query/raw.py

query_product_typename = """query product($productId: String!) {
    product(productId: $productId) {
        __typename
    }
}"""

query_product_with_field = """query product($productId: String!) {
    product(productId: $productId) {
        __typename
        ... on Product {
            productId
            productName
            destinationId
            shortDescription
            cancellationType
            cancellationWindow
            minGroupSize
            openDateTicket
            collectPhysicalTicket
            confirmationType
            voucherType
            priceRangeFrom
            priceRangeTo
            latitude
            longitude
            address
        }
        ... on PelagoError {
            errorMessage
            code
        }
    }
}"""
