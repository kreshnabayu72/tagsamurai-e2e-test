---
id: TC-FA-CF-E2E-069-kunci-decimal-places-pada-edit-dasar
title: "Kunci Decimal Places pada Edit: Tooltip dan Syarat Kunci"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-241
  - TC-FA-CF-242
  - TC-FA-CF-243
  - TC-FA-CF-244
coverage:
  web: automated
---

# Kunci Decimal Places pada Edit: Tooltip dan Syarat Kunci

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General): dipakai `Rated Power` (Numeric 1 Decimal Place, bernilai pada aset A1), `Global Only Numeric` (Numeric 0 Decimal Places General Global `5`, tanpa nilai aset), `Deleted Only Metric` (Numeric 2 Decimal Places, bernilai hanya pada aset A3 berstatus deleted), dan `Empty Metric` (Numeric 2 Decimal Places General, tanpa nilai). Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` memulihkan field baseline yang diubah spec (`Empty Metric` kembali ke Decimal Places baseline) dan membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE.
- Kemampuan teknis: hover; fokus keyboard (Tab) pada radio.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- State global: tidak ada yang diubah selain data Company Nilai yang dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-241: Decimal Places terkunci disabled dengan tooltip saat hover dan fokus keyboard

2. Klik row action `⋯` > `Edit` pada baris `Rated Power`
3. Verifikasi radio Decimal Places tampil (visible)
4. Verifikasi radio Decimal Places disabled
5. Arahkan kursor ke radio Decimal Places
6. Verifikasi tooltip `Decimal places can't be changed because assets already have values for this field.` tampil saat hover
7. Pindahkan kursor keluar dari radio Decimal Places
8. Pindahkan fokus keyboard ke radio Decimal Places
9. Verifikasi tooltip `Decimal places can't be changed because assets already have values for this field.` tampil saat fokus keyboard
10. Klik icon close `[✕]`

### TC-FA-CF-243: Global Value tidak memicu kunci Decimal Places

11. Klik row action `⋯` > `Edit` pada baris `Global Only Numeric`
12. Verifikasi radio Decimal Places enabled
13. Klik icon close `[✕]`

### TC-FA-CF-244: Nilai pada aset berstatus deleted tidak mengunci Decimal Places

14. Klik row action `⋯` > `Edit` pada baris `Deleted Only Metric`
15. Verifikasi radio Decimal Places enabled
16. Klik icon close `[✕]`

### TC-FA-CF-242: Decimal Places bebas dipilih saat tidak ada aset yang menyimpan nilai

17. Klik row action `⋯` > `Edit` pada baris `Empty Metric`
18. Verifikasi radio Decimal Places enabled
19. Pilih Decimal Places `1 (.0)`
20. Klik `[Save]`
21. Verifikasi toast sukses `Success, custom field has been updated.` tampil
22. Verifikasi kolom Value Setting baris `Empty Metric` menampilkan `1 Decimal Place`

## Notes

- Urutan TC di spec: 241, 243, 244, 242. Kasus yang hanya membaca (241, 243, 244) berjalan lebih dulu dan modal ditutup dengan `[✕]` tanpa perubahan (tanpa dialog `Unsaved Changes`); TC-FA-CF-242 mengubah dan menyimpan `Empty Metric`, sehingga di akhir (bagian 3 prinsip 6).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 100 supaya seluruh baris Company Nilai tampil dan baris target ditemukan tanpa Search), langkah 7 (melepas kursor dari radio supaya tooltip hover hilang sebelum asersi fokus keyboard; bagian 8b butir 5), langkah 10, 13, dan 16 (menutup modal yang tidak diubah).
- Temuan untuk QA:
  - Expected TC-FA-CF-241 b menyebut tooltip tampil "saat hover dan saat fokus keyboard" tanpa menyatakan urutan; spec mengasersinya berurutan (hover lalu fokus) pada modal yang sama.
  - Email Total Control Company Nilai dan env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` yang disediakan tim FE.
