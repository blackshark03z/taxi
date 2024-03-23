def tinh_tien_taxi(so_km, thoi_gian_cho):
  muc_gia_di_chuyen_2km_dau = 10000
  muc_gia_di_chuyen_km_tiep_theo = 15000
  muc_gia_cho_10phut_dau =  5000
  muc_gia_cho_phut_tiep_theo = 7000

  if so_km <= 2:
    gia_di_chuyen = so_km * muc_gia_di_chuyen_2km_dau
  else:
    gia_di_chuyen = 2*muc_gia_di_chuyen_2km_dau + (so_km - 2) * muc_gia_di_chuyen_km_tiep_theo

  if thoi_gian_cho <= 10:
    gia_cho = thoi_gian_cho * muc_gia_cho_10phut_dau
  else:
    gia_cho = 10*muc_gia_cho_10phut_dau + (thoi_gian_cho - 10) * muc_gia_cho_phut_tiep_theo

  return gia_di_chuyen + gia_cho