export const gqlGetOpportunity = `query OpportunityQuery($id: ID, $cdn_links: Boolean) {
  getOpportunity(id: $id) {
    applied_to
    applied_to_with
    applications_close_date
    available_openings
    backgrounds {
      constant_id
      constant_name
      option
      __typename
    }
    branch {
      id
      address_detail {
        id
        city
        country
        __typename
      }
      company {
        id
        name
        profile_photo(cdn_links: $cdn_links)
        __typename
      }
      __typename
    }
    cover_photo(cdn_links: $cdn_links)
    description
    duration
    project_duration
    earliest_start_date
    google_place_id
    home_lc {
      id
      email
      full_name
      parent {
        id
        __typename
      }
      __typename
    }
    id
    is_favourited
    is_gep
    languages {
      constant_id
      constant_name
      option
      __typename
    }
    lat
    latest_end_date
    lng
    legal_info {
      health_insurance_info
      visa_duration
      visa_link
      visa_type
      __typename
    }
    location
    logistics_info {
      accommodation_covered
      accommodation_provided
      food_covered
      __typename
    }
    nationalities {
      constant_id
      constant_name
      option
      __typename
    }
    office_footfall_for_exchange
    openings
    opportunity_cost
    programme {
      id
      short_name_display
      __typename
    }
    remark
    reviews
    role_info {
      selection_process
      learning_points_list
      __typename
    }
    sdg_info {
      id
      sdg_target {
        description
        goal_index
        id
        parent {
          id
          __typename
        }
        target
        __typename
      }
      __typename
    }
    skills {
      constant_id
      constant_name
      option
      __typename
    }
    specifics_info {
      computer
      expected_work_schedule
      ef_test_required
      salary
      salary_currency {
        id
        alphabetic_code
        __typename
      }
      salary_periodicity
      saturday_work
      __typename
    }
    status
    study_levels {
      id
      name
      __typename
    }
    sub_product {
      id
      name
    }
    title
    transparent_fee_details {
      covers_accomodation
      covers_administrative_costs
      covers_leadership_spaces
      covers_pickup
      sponsored_by
      __typename
    }
    __typename
  }
}`;