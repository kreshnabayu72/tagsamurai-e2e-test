---
id: TC-GS-GSET-E2E-025-alur-kombinasi-search-filter-sort-pagination
title: Kombinasi search + filter + sort + pagination
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-68
  - TC-GS-GSET-69
  - TC-GS-GSET-70
  - TC-GS-GSET-71
  - TC-GS-GSET-72
  - TC-GS-GSET-73
  - TC-GS-GSET-74
coverage:
  web: automated
---

# Alur kombinasi keempat kontrol tabel

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Dataset changelog 50+ baris dengan variasi `Action`, `Field`, `Modified By`, dan `Date Modified`.
- Fitur sort diuji terpisah khusus sort (spec 027); di sini sort hanya dipakai sebagai salah satu
  dimensi kombinasi.

## Test Steps

### Search + Filter + Sort + Pagination ditegakkan bersama

1. Buka Modal Changelog
2. Search `Currency`
3. Filter `Date` Excel ± dua minggu yang mencakup baris currency tertentu
4. Sort kolom `Action` ascending
5. Verifikasi hasil dari search + filter benar-benar ter-render dalam urutan sort yang dipilih
6. Lihat halaman berikutnya; verifikasi urutan bertahan melintasi pagination dan tidak hilang search/filter

### Recovery: ubah urutan reset satu persatu

7. Hapus search (klik 🗑 pada search box); verifikasi hasil masih mematuhi filter+sort
8. Clear filter (tombol `[Clear]`); verifikasi hasil mematuhi sort saja
9. Reset sort (klik kolom sampai netral); verifikasi seluruh baris kembali dalam urutan default tanpa
   take efek filter

### Urutan terakhir dalam kombinasi

10. Susun ulang: sort diubah dulu, baru search/filter; verifikasi semua kombinasi menghasilkan hasil yang
    deterministik (urutan perubahan kontrol tidak mengubah hasil akhir)

### Clear search/filter tidak men-trigger save

11. Pastikan tombol `[Save]` tetap non-aktif setelah seluruh kombinasi kontrol pada modal changelog
    selesai dijalankan (struktur modal berbeda dari form utama)

## Notes

- TC-GS-GSET-71-74 membuktikan interaksi keempat kontrol saling menghargai urutan prioritas internal
  yang ditetapkan di PRD §3.4.i; spec menegaskan hasil deterministik terhadap urutan interaksi pengguna.