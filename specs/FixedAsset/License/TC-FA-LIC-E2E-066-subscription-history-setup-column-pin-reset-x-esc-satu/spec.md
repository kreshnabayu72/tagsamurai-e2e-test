---
id: TC-FA-LIC-E2E-066-subscription-history-setup-column-pin-reset-x-esc-satu
title: "Subscription History: Setup Column (Pin dan Unpin per Kolom, Reset to Default, X atau Esc, dan Satu Kolom Tersisa)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-210
  - TC-FA-LIC-211
  - TC-FA-LIC-212
  - TC-FA-LIC-213
coverage:
  web: automated
---
# Subscription History: Setup Column (Pin dan Unpin per Kolom, Reset to Default, X atau Esc, dan Satu Kolom Tersisa)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #13 (Subscription History, hanya dibaca): empat term Subscription lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): SUBS-20270101-00001 (Plan Professional, Type Paid, Status Pending, Plan Owner PT Maju Bersama (Distributor)), SUBS-20260101-00001 (Professional, Paid, Active, PT Maju Bersama (Distributor)), SUBS-20250101-00001 (Professional, Paid, Renewed, PT Maju Bersama (Distributor)), SUBS-20241201-00001 (Enterprise, Trial, Converted, PT ABC (Principal)). Urutan default Start Date terbaru lebih dulu: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001, SUBS-20241201-00001.
- Pemulihan konfigurasi kolom: konfigurasi Setup Column atau Column Visibility yang disimpan spec ini didaftarkan di `suite.md`; hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE).
- Daftar kolom Hideable Visible default (parameter langkah 3 sampai 15): `Subscription ID`, `Plan`, `Type`, `Status`, `Start Date`, `End Date`, `Plan Owner` (tujuh kolom).
- Penutup Setup Column (TC-FA-LIC-212, parameter langkah 23 sampai 30): `(×)` dan Esc.
- Kemampuan teknis: viewport browser disempitkan sehingga tabel Subscription History dapat digeser horizontal (pilihan spec; TC hanya menulis "geser tabel horizontal"), dan dipulihkan pada langkah 38. Pengamatan posisi kolom saat tabel digeser (sticky) disediakan tim FE.
- State yang diubah dan dipulihkan: Pin, visibilitas, dan urutan kolom Setup Column (tiap iterasi memulihkan pada langkah 15; TC-FA-LIC-211 mengakhiri dengan susunan default tersimpan; didaftarkan di `suite.md`) dan viewport.

## Test Steps

1. Klik sub-tab `Subscription History`
2. Sempitkan viewport browser sehingga tabel dapat digeser horizontal

### TC-FA-LIC-210: Pin dan Unpin per kolom

Untuk setiap kolom pada daftar kolom (langkah 3 sampai 15):

3. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
4. Klik ikon Pin pada kolom
5. Klik `[Save]`
6. Geser tabel secara horizontal
7. Verifikasi kolom membeku (sticky) di kiri saat tabel digeser horizontal
8. Muat ulang halaman (F5)
9. Geser tabel secara horizontal
10. Verifikasi kolom tetap membeku (sticky) di kiri setelah F5
11. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
12. Klik ikon Pin pada kolom untuk Unpin
13. Klik `[Save]`
14. Geser tabel secara horizontal
15. Verifikasi kolom tidak lagi membeku (Unpin melepasnya)

### TC-FA-LIC-211: Reset to Default

16. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
17. Hilangkan centang kolom `Plan` dan seret kolom `Type` ke posisi pertama
18. Klik `[Reset to Default]`
19. Verifikasi Live Preview kembali ke susunan default modul
20. Klik `[Save]`
21. Muat ulang halaman (F5)
22. Verifikasi susunan default tersimpan dan bertahan setelah F5

### TC-FA-LIC-212: X atau Esc membuang perubahan

Untuk setiap penutup pada daftar penutup (langkah 23 sampai 30):

23. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
24. Hilangkan centang kolom `Status`
25. Tutup popup dengan penutup (`(×)` atau Esc)
26. Verifikasi modal tertutup
27. Verifikasi tabel memakai konfigurasi tersimpan terakhir (kolom `Status` tetap tampil)
28. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
29. Verifikasi perubahan preview dibuang (kolom `Status` tercentang pada Live Preview)
30. Klik `(×)` untuk menutup popup

### TC-FA-LIC-213: Satu kolom visible tersisa tidak dapat di-uncheck

31. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
32. Hilangkan centang semua kolom kecuali `Subscription ID`
33. Coba hilangkan centang kolom terakhir `Subscription ID`
34. Verifikasi checkbox kolom terakhir disabled
35. Arahkan kursor ke checkbox kolom terakhir
36. Verifikasi tooltip `At least one column must remain visible.`
37. Klik `(×)` untuk menutup popup tanpa menyimpan
38. Pulihkan viewport browser ke ukuran semula

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec ini di atas 35 langkah (38 langkah nominal; 124 langkah setelah ekspansi). Alasan: seluruh blok satu topik (Setup Column Subscription History), satu dataset Pre-setup #13 yang hanya dibaca, tiap blok berdiri sendiri, dan langkah 3 sampai 15 (tujuh iterasi) serta 23 sampai 30 (dua iterasi) diulang dengan parameter di `## Prerequisites`, tanpa langkah bersyarat dan dengan satu `Verifikasi` per klausa (S-01).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (klik sub-tab sebagai aksi deterministik), langkah 2 dan 38 (menyempitkan dan memulihkan viewport), langkah 6, 9, dan 14 (menggeser tabel), dan langkah 12 sampai 13 (Unpin sebagai pemulihan sekaligus bagian Expected "Unpin melepasnya").
- Temuan untuk QA:
  - TC-FA-LIC-210 mengasersi kolom "membeku (sticky) di kiri saat scroll horizontal" tanpa menyebut lebar viewport; spec menyempitkan viewport.
  - TC-FA-LIC-211 menulis "ubah visibilitas dan urutan beberapa kolom" tanpa menyebut kolom; spec menyembunyikan `Plan` dan memindahkan `Type` ke posisi pertama.
  - TC-FA-LIC-212 menulis `(×)` atau Esc sebagai satu langkah; spec menjalankan keduanya sebagai dua iterasi.
  - TC-FA-LIC-213 tidak menyebut kolom yang dipertahankan; spec mempertahankan `Subscription ID`.
  - TC-FA-LIC-210, 211, 212, dan 213 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
