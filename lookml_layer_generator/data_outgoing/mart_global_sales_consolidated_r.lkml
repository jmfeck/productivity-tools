
view: mart_global_sales_consolidated_r {
  sql_table_name: `mtb-eu-datalake-ww-nprd.dnst_commercial_mart.mtb_mart_global_sales_consolidated` ;;

  # -------------------------------
  # Default Dimensions
  # -------------------------------{
  dimension: brand {
    group_label: "Article - Details"
    label: "Brand"
    description: "-"
  }
  
  dimension: apo_location {
    group_label: "Transactional - Details"
    label: "Apo Location"
    description: "-"
  }
  
  dimension: batch {
    group_label: "Transactional - Details"
    label: "Batch"
    description: "-"
  }
  
  dimension: boutique_ear {
    group_label: "Customer - Boutique"
    label: "Boutique Ear"
    description: "-"
  }
  
  dimension: calendar_day {
    group_label: "Time - Calendar"
    label: "Calendar Day"
    description: "-"
  }
  
  dimension: calendar_day_week {
    group_label: "Time - Calendar"
    label: "Calendar Day Week"
    description: "-"
  }
  
  dimension: calendar_month {
    group_label: "Time - Calendar"
    label: "Calendar Month"
    description: "-"
  }
  
  dimension: calendar_year {
    group_label: "Time - Calendar"
    label: "Calendar Year"
    description: "-"
  }
  
  dimension: calendar_year_month {
    group_label: "Time - Calendar"
    label: "Calendar Year Month"
    description: "-"
  }
  
  dimension: calendar_year_week {
    group_label: "Time - Calendar"
    label: "Calendar Year Week"
    description: "-"
  }
  
  dimension: fiscal_period {
    group_label: "Time - Fiscal"
    label: "Fiscal Period"
    description: "-"
  }
  
  dimension: fiscal_variant {
    group_label: "Transactional - Details"
    label: "Fiscal Variant"
    description: "-"
  }
  
  dimension: fiscal_year {
    group_label: "Time - Fiscal"
    label: "Fiscal Year"
    description: "-"
  }
  
  dimension: channel {
    group_label: "Customer - Channel"
    label: "Channel"
    description: "-"
  }
  
  dimension: channel_txt {
    group_label: "Customer - Channel"
    label: "Channel Txt"
    description: "-"
  }
  
  dimension: co_document_number {
    group_label: "Transactional - Details"
    label: "Co Document Number"
    description: "-"
  }
  
  dimension: commercial_zone {
    group_label: "Transactional - Details"
    label: "Commercial Zone"
    description: "-"
  }
  
  dimension: company_code {
    group_label: "Transactional - Details"
    label: "Company Code"
    description: "-"
  }
  
  dimension: consignment_flag {
    group_label: "Transactional - Details"
    label: "Consignment Flag"
    description: "-"
  }
  
  dimension: controlling_area {
    group_label: "Transactional - Details"
    label: "Controlling Area"
    description: "-"
  }
  
  dimension: controlling_view_posted {
    group_label: "Transactional - Details"
    label: "Controlling View Posted"
    description: "-"
  }
  
  dimension: currency {
    group_label: "Transactional - Currency & FX"
    label: "Currency"
    description: "-"
  }
  
  dimension: currency_nrsp {
    group_label: "Transactional - Currency & FX"
    label: "Currency Nrsp"
    description: "-"
  }
  
  dimension: customer_global {
    group_label: "Customer - Details"
    label: "Customer Global"
    description: "-"
  }
  
  dimension: customer_group {
    group_label: "Customer - Details"
    label: "Customer Group"
    description: "-"
  }
  
  dimension: destination_country {
    group_label: "Transactional - Details"
    label: "Destination Country"
    description: "-"
  }
  
  dimension: ecom_channel {
    group_label: "Customer - Channel"
    label: "Ecom Channel"
    description: "-"
  }
  
  dimension: fa_collection_posted {
    group_label: "Article - Details"
    label: "Fa Collection Posted"
    description: "-"
  }
  
  dimension: fa_product_seasonality_posted {
    group_label: "Article - Details"
    label: "Fa Product Seasonality Posted"
    description: "-"
  }
  
  dimension: fa_season_posted {
    group_label: "Article - Details"
    label: "Fa Season Posted"
    description: "-"
  }
  
  dimension: fa_theme_posted {
    group_label: "Article - Details"
    label: "Fa Theme Posted"
    description: "-"
  }
  
  dimension: global_invoice {
    group_label: "Transactional - Details"
    label: "Global Invoice"
    description: "-"
  }
  
  dimension: global_network {
    group_label: "Transactional - Details"
    label: "Global Network"
    description: "-"
  }
  
  dimension: global_pos {
    group_label: "Transactional - Details"
    label: "Global Pos"
    description: "-"
  }
  
  dimension: global_pos_id {
    group_label: "Transactional - Details"
    label: "Global Pos Id"
    description: "-"
  }
  
  dimension: global_site_ear {
    group_label: "Transactional - Details"
    label: "Global Site Ear"
    description: "-"
  }
  
  dimension: leading_object {
    group_label: "Transactional - Details"
    label: "Leading Object"
    description: "-"
  }
  
  dimension: order_reason {
    group_label: "Transactional - Details"
    label: "Order Reason"
    description: "-"
  }
  
  dimension: pos_booster {
    group_label: "Transactional - Details"
    label: "Pos Booster"
    description: "-"
  }
  
  dimension: posting_period {
    group_label: "Time - Fiscal"
    label: "Posting Period"
    description: "-"
  }
  
  dimension: product_segment_posted {
    group_label: "Article - Details"
    label: "Product Segment Posted"
    description: "-"
  }
  
  dimension: profit_center {
    group_label: "Transactional - Details"
    label: "Profit Center"
    description: "-"
  }
  
  dimension: record_type {
    group_label: "Transactional - Details"
    label: "Record Type"
    description: "-"
  }
  
  dimension: reference_document_number {
    group_label: "Transactional - Details"
    label: "Reference Document Number"
    description: "-"
  }
  
  dimension: reporting_entity {
    group_label: "Transactional - Details"
    label: "Reporting Entity"
    description: "-"
  }
  
  dimension: reporting_entity_txt {
    group_label: "Transactional - Details"
    label: "Reporting Entity Txt"
    description: "-"
  }
  
  dimension: sales_associate {
    group_label: "Transactional - Details"
    label: "Sales Associate"
    description: "-"
  }
  
  dimension: sales_doc_type {
    group_label: "Transactional - Details"
    label: "Sales Doc Type"
    description: "-"
  }
  
  dimension: sales_document {
    group_label: "Transactional - Details"
    label: "Sales Document"
    description: "-"
  }
  
  dimension: sales_organization {
    group_label: "Transactional - Details"
    label: "Sales Organization"
    description: "-"
  }
  
  dimension: sales_representative {
    group_label: "Transactional - Details"
    label: "Sales Representative"
    description: "-"
  }
  
  dimension: sales_representative_global {
    group_label: "Transactional - Details"
    label: "Sales Representative Global"
    description: "-"
  }
  
  dimension: serial_number {
    group_label: "Transactional - Details"
    label: "Serial Number"
    description: "-"
  }
  
  dimension: sold_to_party {
    group_label: "Transactional - Details"
    label: "Sold To Party"
    description: "-"
  }
  
  dimension: ship_to_party {
    group_label: "Transactional - Details"
    label: "Ship To Party"
    description: "-"
  }
  
  dimension: source_partition {
    group_label: "Transactional - Details"
    label: "Source Partition"
    description: "-"
  }
  
  dimension: source_system {
    group_label: "Transactional - Details"
    label: "Source System"
    description: "-"
  }
  
  dimension: source_table {
    group_label: "Transactional - Details"
    label: "Source Table"
    description: "-"
  }
  
  dimension: unit_of_measure {
    group_label: "Transactional - Details"
    label: "Unit Of Measure"
    description: "-"
  }
  
  dimension: article {
    group_label: "Article - Details"
    label: "Article"
    description: "-"
  }
  
  dimension: commercial_group {
    group_label: "Customer - GBU"
    label: "Commercial Group"
    description: "-"
  }
  
  dimension: mtb_channel_official {
    group_label: "Customer - Channel"
    label: "Channel Official"
    description: "-"
  }
  
  dimension: mtb_channel_official_short {
    group_label: "Customer - Channel"
    label: "Channel Official Short"
    description: "-"
  }
  
  dimension: mtb_channel_dtc_flag {
    group_label: "Customer - Channel"
    label: "Channel DTC Flag"
    description: "-"
  }
  
  dimension: article_txt {
    group_label: "Article - Details"
    label: "Article Txt"
    description: "-"
  }
  
  dimension: mtb_ah_level0 {
    group_label: "Article - Hierarchy"
    label: "AH Level0"
    description: "-"
  }
  
  dimension: mtb_ah_level0_txt {
    group_label: "Article - Hierarchy"
    label: "AH Level0 Txt"
    description: "-"
  }
  
  dimension: mtb_ah_level0_rank {
    group_label: "Article - Hierarchy"
    label: "AH Level0 Rank"
    description: "-"
  }
  
  dimension: mtb_ah_level1 {
    group_label: "Article - Hierarchy"
    label: "AH Level1"
    description: "-"
  }
  
  dimension: mtb_ah_level1_txt {
    group_label: "Article - Hierarchy"
    label: "AH Level1 Txt"
    description: "-"
  }
  
  dimension: mtb_ah_level1_rank {
    group_label: "Article - Hierarchy"
    label: "AH Level1 Rank"
    description: "-"
  }
  
  dimension: mtb_ah_level2 {
    group_label: "Article - Hierarchy"
    label: "AH Level2"
    description: "-"
  }
  
  dimension: mtb_ah_level2_txt {
    group_label: "Article - Hierarchy"
    label: "AH Level2 Txt"
    description: "-"
  }
  
  dimension: mtb_ah_level2_rank {
    group_label: "Article - Hierarchy"
    label: "AH Level2 Rank"
    description: "-"
  }
  
  dimension: mtb_ah_level3 {
    group_label: "Article - Hierarchy"
    label: "AH Level3"
    description: "-"
  }
  
  dimension: mtb_ah_level3_txt {
    group_label: "Article - Hierarchy"
    label: "AH Level3 Txt"
    description: "-"
  }
  
  dimension: mtb_ah_level3_rank {
    group_label: "Article - Hierarchy"
    label: "AH Level3 Rank"
    description: "-"
  }
  
  dimension: mtb_ah_level4 {
    group_label: "Article - Hierarchy"
    label: "AH Level4"
    description: "-"
  }
  
  dimension: mtb_ah_level4_txt {
    group_label: "Article - Hierarchy"
    label: "AH Level4 Txt"
    description: "-"
  }
  
  dimension: mtb_ah_level4_rank {
    group_label: "Article - Hierarchy"
    label: "AH Level4 Rank"
    description: "-"
  }
  
  dimension: mtb_ah_level5 {
    group_label: "Article - Hierarchy"
    label: "AH Level5"
    description: "-"
  }
  
  dimension: mtb_ah_level5_txt {
    group_label: "Article - Hierarchy"
    label: "AH Level5 Txt"
    description: "-"
  }
  
  dimension: mtb_ah_level5_rank {
    group_label: "Article - Hierarchy"
    label: "AH Level5 Rank"
    description: "-"
  }
  
  dimension: mtb_ah_level6 {
    group_label: "Article - Hierarchy"
    label: "AH Level6"
    description: "-"
  }
  
  dimension: mtb_ah_level6_txt {
    group_label: "Article - Hierarchy"
    label: "AH Level6 Txt"
    description: "-"
  }
  
  dimension: mtb_ah_level6_rank {
    group_label: "Article - Hierarchy"
    label: "AH Level6 Rank"
    description: "-"
  }
  
  dimension: mtb_ah_level7 {
    group_label: "Article - Hierarchy"
    label: "AH Level7"
    description: "-"
  }
  
  dimension: mtb_ah_level7_txt {
    group_label: "Article - Hierarchy"
    label: "AH Level7 Txt"
    description: "-"
  }
  
  dimension: mtb_ah_level7_rank {
    group_label: "Article - Hierarchy"
    label: "AH Level7 Rank"
    description: "-"
  }
  
  dimension: mtb_merch_launch_date_revised {
    group_label: "Article - Merchandising"
    label: "Launch Date Revised"
    description: "-"
  }
  
  dimension: mtb_merch_category_level1 {
    group_label: "Article - Merchandising"
    label: "Category Level1"
    description: "-"
  }
  
  dimension: mtb_merch_category_level2 {
    group_label: "Article - Merchandising"
    label: "Category Level2"
    description: "-"
  }
  
  dimension: mtb_merch_collection_line_level1 {
    group_label: "Article - Merchandising"
    label: "Collection Line Level1"
    description: "-"
  }
  
  dimension: mtb_merch_collection_line_level2 {
    group_label: "Article - Merchandising"
    label: "Collection Line Level2"
    description: "-"
  }
  
  dimension: mtb_merch_function_level1 {
    group_label: "Article - Merchandising"
    label: "Function Level1"
    description: "-"
  }
  
  dimension: mtb_merch_function_level2 {
    group_label: "Article - Merchandising"
    label: "Function Level2"
    description: "-"
  }
  
  dimension: mtb_merch_function_level3 {
    group_label: "Article - Merchandising"
    label: "Function Level3"
    description: "-"
  }
  
  dimension: mtb_merch_archetype {
    group_label: "Article - Merchandising"
    label: "Archetype"
    description: "-"
  }
  
  dimension: mtb_merch_material_level1 {
    group_label: "Article - Merchandising"
    label: "Material Level1"
    description: "-"
  }
  
  dimension: mtb_merch_material_level2 {
    group_label: "Article - Merchandising"
    label: "Material Level2"
    description: "-"
  }
  
  dimension: mtb_merch_material_level3 {
    group_label: "Article - Merchandising"
    label: "Material Level3"
    description: "-"
  }
  
  dimension: mtb_merch_price_level1 {
    group_label: "Article - Merchandising"
    label: "Price Level1"
    description: "-"
  }
  
  dimension: mtb_merch_price_level2 {
    group_label: "Article - Merchandising"
    label: "Price Level2"
    description: "-"
  }
  
  dimension: mtb_merch_color_level1 {
    group_label: "Article - Merchandising"
    label: "Color Level1"
    description: "-"
  }
  
  dimension: mtb_merch_color_level2 {
    group_label: "Article - Merchandising"
    label: "Color Level2"
    description: "-"
  }
  
  dimension: mtb_merch_color_level3 {
    group_label: "Article - Merchandising"
    label: "Color Level3"
    description: "-"
  }
  
  dimension: mtb_merch_product_cluster {
    group_label: "Article - Merchandising"
    label: "Product Cluster"
    description: "-"
  }
  
  dimension: mtb_merch_season_level1 {
    group_label: "Article - Merchandising"
    label: "Season Level1"
    description: "-"
  }
  
  dimension: mtb_merch_season_level2 {
    group_label: "Article - Merchandising"
    label: "Season Level2"
    description: "-"
  }
  
  dimension: mtb_merch_launch_financial_year {
    group_label: "Article - Merchandising"
    label: "Launch Financial Year"
    description: "-"
  }
  
  dimension: mtb_merch_campaign {
    group_label: "Article - Merchandising"
    label: "Campaign"
    description: "-"
  }
  
  dimension: mtb_gbu_level6 {
    group_label: "Customer - GBU"
    label: "GBU Level6"
    description: "-"
  }
  
  dimension: mtb_gbu_level6_txt {
    group_label: "Customer - GBU"
    label: "GBU Level6 Txt"
    description: "-"
  }
  
  dimension: mtb_gbu_level6_rank {
    group_label: "Customer - GBU"
    label: "GBU Level6 Rank"
    description: "-"
  }
  
  dimension: mtb_gbu_level5 {
    group_label: "Customer - GBU"
    label: "GBU Level5"
    description: "-"
  }
  
  dimension: mtb_gbu_level5_txt {
    group_label: "Customer - GBU"
    label: "GBU Level5 Txt"
    description: "-"
  }
  
  dimension: mtb_gbu_level5_rank {
    group_label: "Customer - GBU"
    label: "GBU Level5 Rank"
    description: "-"
  }
  
  dimension: mtb_gbu_level4 {
    group_label: "Customer - GBU"
    label: "GBU Level4"
    description: "-"
  }
  
  dimension: mtb_gbu_level4_txt {
    group_label: "Customer - GBU"
    label: "GBU Level4 Txt"
    description: "-"
  }
  
  dimension: mtb_gbu_level4_rank {
    group_label: "Customer - GBU"
    label: "GBU Level4 Rank"
    description: "-"
  }
  
  dimension: mtb_gbu_level3 {
    group_label: "Customer - GBU"
    label: "GBU Level3"
    description: "-"
  }
  
  dimension: mtb_gbu_level3_txt {
    group_label: "Customer - GBU"
    label: "GBU Level3 Txt"
    description: "-"
  }
  
  dimension: mtb_gbu_level3_rank {
    group_label: "Customer - GBU"
    label: "GBU Level3 Rank"
    description: "-"
  }
  
  dimension: mtb_gbu_level2 {
    group_label: "Customer - GBU"
    label: "GBU Level2"
    description: "-"
  }
  
  dimension: mtb_gbu_level2_txt {
    group_label: "Customer - GBU"
    label: "GBU Level2 Txt"
    description: "-"
  }
  
  dimension: mtb_gbu_level2_rank {
    group_label: "Customer - GBU"
    label: "GBU Level2 Rank"
    description: "-"
  }
  
  dimension: mtb_gbu_level1 {
    group_label: "Customer - GBU"
    label: "GBU Level1"
    description: "-"
  }
  
  dimension: mtb_gbu_level1_txt {
    group_label: "Customer - GBU"
    label: "GBU Level1 Txt"
    description: "-"
  }
  
  dimension: mtb_gbu_level1_rank {
    group_label: "Customer - GBU"
    label: "GBU Level1 Rank"
    description: "-"
  }
  
  dimension: mtb_gbu_level6_hex {
    group_label: "Customer - GBU"
    label: "GBU Level6 Hex"
    description: "-"
  }
  
  dimension: boutique_txt {
    group_label: "Customer - Boutique"
    label: "Boutique Txt"
    description: "-"
  }
  
  dimension: mtb_boutique_type {
    group_label: "Customer - Boutique"
    label: "Boutique Type"
    description: "-"
  }
  
  dimension: mtb_boutique_outlet_flag {
    group_label: "Customer - Boutique"
    label: "Boutique Outlet Flag"
    description: "-"
  }
  
  dimension: mtb_boutique_finance_status {
    group_label: "Customer - Boutique"
    label: "Boutique Finance Status"
    description: "-"
  }
  
  dimension: mtb_boutique_country {
    group_label: "Customer - Boutique"
    label: "Boutique Country"
    description: "-"
  }
  
  dimension: mtb_boutique_commercial_status {
    group_label: "Customer - Boutique"
    label: "Boutique Commercial Status"
    description: "-"
  }
  
  dimension: mtb_boutique_city {
    group_label: "Customer - Boutique"
    label: "Boutique City"
    description: "-"
  }
  
  dimension: mtb_boutique_landlord_name {
    group_label: "Customer - Boutique"
    label: "Boutique Landlord Name"
    description: "-"
  }
  
  dimension: mtb_boutique_first_opening_date {
    group_label: "Customer - Boutique"
    label: "Boutique First Opening Date"
    description: "-"
  }
  
  dimension: mtb_boutique_last_renovation_date {
    group_label: "Customer - Boutique"
    label: "Boutique Last Renovation Date"
    description: "-"
  }
  
  dimension: mtb_boutique_reopening_date {
    group_label: "Customer - Boutique"
    label: "Boutique Reopening Date"
    description: "-"
  }
  
  dimension: mtb_boutique_closing_date {
    group_label: "Customer - Boutique"
    label: "Boutique Closing Date"
    description: "-"
  }
  
  dimension: mtb_boutique_concept {
    group_label: "Customer - Boutique"
    label: "Boutique Concept"
    description: "-"
  }
  
  dimension: mtb_boutique_pos_type {
    group_label: "Customer - Boutique"
    label: "Boutique Pos Type"
    description: "-"
  }
  
  dimension: mtb_boutique_condition_notes {
    group_label: "Customer - Boutique"
    label: "Boutique Condition Notes"
    description: "-"
  }
  
  dimension: mtb_boutique_location_type {
    group_label: "Customer - Boutique"
    label: "Boutique Location Type"
    description: "-"
  }
  
  dimension: mtb_boutique_floor {
    group_label: "Customer - Boutique"
    label: "Boutique Floor"
    description: "-"
  }
  
  dimension: mtb_boutique_area_total_sqm {
    group_label: "Customer - Boutique"
    label: "Boutique Area Total Sqm"
    description: "-"
  }
  
  dimension: mtb_boutique_area_commercial_sqm {
    group_label: "Customer - Boutique"
    label: "Boutique Area Commercial Sqm"
    description: "-"
  }
  
  dimension: mtb_boutique_area_backoffice_sqm {
    group_label: "Customer - Boutique"
    label: "Boutique Area Backoffice Sqm"
    description: "-"
  }
  
  dimension: mtb_boutique_lease_terms {
    group_label: "Customer - Boutique"
    label: "Boutique Lease Terms"
    description: "-"
  }
  
  dimension: mtb_boutique_lease_expiry_date {
    group_label: "Customer - Boutique"
    label: "Boutique Lease Expiry Date"
    description: "-"
  }
  
  dimension: mtb_boutique_fixed_rent_euro {
    group_label: "Customer - Boutique"
    label: "Boutique Fixed Rent Euro"
    description: "-"
  }
  
  dimension: mtb_boutique_break_point_of_sales_euro {
    group_label: "Customer - Boutique"
    label: "Boutique Break Point Of Sales Euro"
    description: "-"
  }
  
  dimension: mtb_boutique_effective_variable_rent {
    group_label: "Customer - Boutique"
    label: "Boutique Effective Variable Rent"
    description: "-"
  }
  
  dimension: mtb_boutique_neighbour_front {
    group_label: "Customer - Boutique"
    label: "Boutique Neighbour Front"
    description: "-"
  }
  
  dimension: mtb_boutique_neighbour_right {
    group_label: "Customer - Boutique"
    label: "Boutique Neighbour Right"
    description: "-"
  }
  
  dimension: mtb_boutique_neighbour_left {
    group_label: "Customer - Boutique"
    label: "Boutique Neighbour Left"
    description: "-"
  }
  
  dimension: mtb_boutique_has_traffic_counter_flag {
    group_label: "Customer - Boutique"
    label: "Boutique Has Traffic Counter Flag"
    description: "-"
  }
  
  dimension: mtb_boutique_nbv_last_fiscal_year_euro {
    group_label: "Customer - Boutique"
    label: "Boutique Nbv Last Fiscal Year Euro"
    description: "-"
  }
  
  dimension: mtb_boutique_fte {
    group_label: "Customer - Boutique"
    label: "Boutique Fte"
    description: "-"
  }
  
  dimension: rsp_price_de_eur {
    group_label: "Article - Details"
    label: "RSP Price De Eur"
    description: "-"
  }
  
  dimension: dms_front_picture_url {
    group_label: "Article - Details"
    label: "Article Front Picture Url"
    description: "-"
  }
  
  dimension: mtb_ah_leveln_key {
    group_label: "Transactional - Details"
    label: "AH Leveln Key"
    description: "-"
  }
  
  dimension: mtb_ah_n {
    group_label: "Transactional - Details"
    label: "AH N"
    description: "-"
  }
  
  ### }
  
  # -------------------------------
  # Default Measures
  # -------------------------------{
  measure: sellin_qty {
    group_label: "Sellin - Quantity"
    label: "Sellin Quantity"
    description: "-"
    type: sum
    sql: ${sellin_qty} ;;
    value_format_name: value_human_read
  }
  
  measure: sellin_rsp {
    group_label: "Sellin - Local Currency"
    label: "Sellin RSP"
    description: "-"
    type: sum
    sql: ${sellin_rsp} ;;
    value_format_name: value_human_read
  }
  
  measure: sellin_invoiced_before_discount {
    group_label: "Sellin - Local Currency"
    label: "Sellin Invoiced Before Discount"
    description: "-"
    type: sum
    sql: ${sellin_invoiced_before_discount} ;;
    value_format_name: value_human_read
  }
  
  measure: sellin_discount {
    group_label: "Sellin - Local Currency"
    label: "Sellin Discount"
    description: "-"
    type: sum
    sql: ${sellin_discount} ;;
    value_format_name: value_human_read
  }
  
  measure: sellin_invoiced {
    group_label: "Sellin - Local Currency"
    label: "Sellin Invoiced"
    description: "-"
    type: sum
    sql: ${sellin_invoiced} ;;
    value_format_name: value_human_read
  }
  
  measure: sellin_net {
    group_label: "Sellin - Local Currency"
    label: "Sellin Net"
    description: "-"
    type: sum
    sql: ${sellin_net} ;;
    value_format_name: value_human_read
  }
  
  measure: sellout_qty {
    group_label: "Sellout - Quantity"
    label: "Sellout Quantity"
    description: "-"
    type: sum
    sql: ${sellout_qty} ;;
    value_format_name: value_human_read
  }
  
  measure: sellout_nrsp {
    group_label: "Sellout - Local Currency"
    label: "Sellout NRSP"
    description: "-"
    type: sum
    sql: ${sellout_nrsp} ;;
    value_format_name: value_human_read
  }
  
  measure: sellout_dealer_cost {
    group_label: "Sellout - Local Currency"
    label: "Sellout Dealer Cost"
    description: "-"
    type: sum
    sql: ${sellout_dealer_cost} ;;
    value_format_name: value_human_read
  }
  
  measure: sellout_net {
    group_label: "Sellout - Local Currency"
    label: "Sellout Net"
    description: "-"
    type: sum
    sql: ${sellout_net} ;;
    value_format_name: value_human_read
  }
  
  measure: full_sellout_qty {
    group_label: "Sellout - Quantity"
    label: "Full Sellout Quantity"
    description: "-"
    type: sum
    sql: ${full_sellout_qty} ;;
    value_format_name: value_human_read
  }
  
  measure: full_sellout_nrsp {
    group_label: "Sellout - Local Currency"
    label: "Full Sellout NRSP"
    description: "-"
    type: sum
    sql: ${full_sellout_nrsp} ;;
    value_format_name: value_human_read
  }
  
  measure: mtb_goal_sellin_invoiced {
    group_label: "Sellin - Local Currency"
    label: "Goal Sellin Invoiced"
    description: "-"
    type: sum
    sql: ${mtb_goal_sellin_invoiced} ;;
    value_format_name: value_human_read
  }
  
  ### }
  
  
}
