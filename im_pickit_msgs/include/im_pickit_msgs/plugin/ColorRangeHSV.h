#define IM_PICKIT_MSGS_MESSAGE_COLORRANGEHSV_PLUGIN_CLASS_BODY \
  bool operator==(const ColorRangeHSV_& rhs) const { \
    const double EPS = 0.0001; \
    return std::abs(h_min - rhs.h_min) < EPS && std::abs(h_max - rhs.h_max) < EPS && \
           std::abs(s_min - rhs.s_min) < EPS && std::abs(s_max - rhs.s_max) < EPS && \
           std::abs(v_min - rhs.v_min) < EPS && std::abs(v_max - rhs.v_max) < EPS; \
  } \
  bool operator!=(const ColorRangeHSV_& rhs) const { \
    return !operator==(rhs); \
  }
