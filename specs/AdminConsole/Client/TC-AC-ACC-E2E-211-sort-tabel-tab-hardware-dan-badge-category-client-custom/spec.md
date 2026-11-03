---
id: TC-AC-ACC-E2E-211-sort-tabel-tab-hardware-dan-badge-category-client-custom
title: "Tab Hardware Client Custom: Sort Hardware List, Quota, Purchase History dan Badge Category Terpotong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-783
  - TC-AC-ACC-839
  - TC-AC-ACC-840
  - TC-AC-ACC-814
coverage:
  web: automated
---

# Tab Hardware Client Custom: Sort Hardware List, Quota, Purchase History dan Badge Category Terpotong

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A3): C-DTL-1 "PT Uji Tabel Detail". Hardware List: Handheld Reader / Brand Alfa / HR-200 / Qty 12; Handheld Reader / Brand Beta / HB-1 / Qty 3; Industrial Handheld Reader / Brand Gamma / HG-9 / Qty 5. Quota Hardware (Type, Total Quota/Used/Available): Handheld Reader RFID 20/15/5; Industrial Handheld Reader RFID 12/5/7; Smart Fixed Reader NFC 4/4/0. Purchase History Hardware: Qty 20 Handheld Reader CV Mitra Sejati Andi Wijaya (02 Feb 2026); Qty 12 Industrial Handheld Reader CV Mitra Sejati Budi Santoso (14 Apr 2026); Qty 4 Smart Fixed Reader PT Distribusi Nusantara Citra Dewi (30 Jun 2026). Category "Industrial Handheld Reader" (26 karakter; hierarki Handheld Devices > Industrial Handheld Reader) dan "Handheld Reader" (15 karakter). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya. Spec tidak mengubah C-DTL-1.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-783: Sort Hardware List: urutan awal default Category A-Z serta kolom Brand dan Model/Type

1. Ketik Search `PT Uji Tabel Detail`, tekan Enter
2. Klik Company Name "PT Uji Tabel Detail" untuk membuka Detail
3. Klik Tab `Hardware`
4. Verifikasi urutan awal Hardware List (default Category A-Z): Brand Alfa (HR-200) dan Brand Beta (HB-1) (Handheld Reader) pada posisi 1 dan 2, lalu Brand Gamma (HG-9) (Industrial Handheld Reader) pada posisi 3
5. Klik header kolom Brand satu kali
6. Verifikasi Brand ascending: Brand Alfa, Brand Beta, Brand Gamma
7. Klik header kolom Brand untuk kedua kali
8. Verifikasi Brand descending: Brand Gamma, Brand Beta, Brand Alfa
9. Klik header kolom Brand untuk ketiga kali
10. Verifikasi indikator sort Brand nonaktif dan urutan kembali ke default Category A-Z
11. Klik header kolom Model/Type satu kali
12. Verifikasi Model/Type ascending: HB-1 (Brand Beta), HG-9 (Brand Gamma), HR-200 (Brand Alfa)
13. Klik header kolom Model/Type untuk kedua kali
14. Verifikasi Model/Type descending: HR-200 (Brand Alfa), HG-9 (Brand Gamma), HB-1 (Brand Beta)
15. Klik header kolom Model/Type untuk ketiga kali
16. Verifikasi indikator sort Model/Type nonaktif dan urutan kembali ke default Category A-Z

### TC-AC-ACC-839: Sort Quota Hardware: default Category A-Z dan kolom Total Quota, Used, Available, Type

17. Verifikasi urutan awal tabel Quota: Handheld Reader, Industrial Handheld Reader, Smart Fixed Reader
18. Klik header Total Quota
19. Verifikasi Total Quota klik 1: Smart Fixed Reader (4), Industrial Handheld Reader (12), Handheld Reader (20)
20. Klik header Used
21. Verifikasi Used klik 1: Smart Fixed Reader (4), Industrial Handheld Reader (5), Handheld Reader (15)
22. Klik header Available
23. Verifikasi Available klik 1: Smart Fixed Reader (0), Handheld Reader (5), Industrial Handheld Reader (7)
24. Klik header Type
25. Verifikasi Type klik 1: Smart Fixed Reader (NFC) pada posisi 1, lalu Handheld Reader dan Industrial Handheld Reader (RFID) pada posisi 2 dan 3

### TC-AC-ACC-840: Sort Purchase History Hardware kolom Qty, Category, Source, dan Action by

26. Verifikasi urutan awal tabel Purchase History Hardware (Date terbaru): Qty 4, 12, 20
27. Klik header Qty
28. Verifikasi Qty klik 1: Qty 4, 12, 20
29. Klik header Qty lagi
30. Verifikasi Qty klik 2: Qty 20, 12, 4
31. Klik header Category
32. Verifikasi Category klik 1: Handheld Reader (Qty 20), Industrial Handheld Reader (Qty 12), Smart Fixed Reader (Qty 4)
33. Klik header Source
34. Verifikasi Source klik 1: Qty 20 dan Qty 12 (CV Mitra Sejati) pada posisi 1 dan 2, lalu Qty 4 (PT Distribusi Nusantara) pada posisi 3
35. Klik header Action by
36. Verifikasi Action by klik 1: Qty 20 (Andi Wijaya), Qty 12 (Budi Santoso), Qty 4 (Citra Dewi)

### TC-AC-ACC-814: Badge Category di Quota Hardware dan Purchase History Hardware: truncate nama panjang dan hover hierarki lengkap

37. Lihat badge Category pada baris Total Quota 12 di tabel Quota
38. Verifikasi badge Category pada Quota berseverity primary dan menampilkan "Industrial H..dheld Reader"
39. Arahkan kursor ke badge Category pada baris Total Quota 12
40. Verifikasi tooltip badge Category menampilkan "Handheld Devices > Industrial Handheld Reader"
41. Lihat badge Category pada baris Qty 12 di tabel Purchase History Hardware
42. Verifikasi badge Category pada Purchase History Hardware berseverity primary dan menampilkan "Industrial H..dheld Reader"
43. Arahkan kursor ke badge Category pada baris Qty 12 di Purchase History Hardware
44. Verifikasi tooltip badge Category menampilkan "Handheld Devices > Industrial Handheld Reader"
45. Lihat badge Category "Handheld Reader" pada tabel Quota
46. Verifikasi badge "Handheld Reader" tampil utuh tanpa pemotongan

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa pengurutan tabel pada satu dataset, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: badge Category Hardware List nama panjang pada C-01 (TC-292) ada di spec 207; id TC masing-masing tetap satu spec.
- Temuan untuk QA (S-15): Post Condition seluruh TC `-` sehingga tidak diasersi. Sort Brand dan Model/Type TC-783 mengabaikan urutan antar baris Brand Alfa dan Brand Beta pada urutan awal (sama Category) sesuai Expected.
