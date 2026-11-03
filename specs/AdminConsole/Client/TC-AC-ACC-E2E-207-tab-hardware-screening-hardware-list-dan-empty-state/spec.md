---
id: TC-AC-ACC-E2E-207-tab-hardware-screening-hardware-list-dan-empty-state
title: "Tab Hardware: Screening Hardware List, Toolbar per Section, Badge, Kolom Photo, Panel Filter, dan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-290
  - TC-AC-ACC-468
  - TC-AC-ACC-291
  - TC-AC-ACC-295
  - TC-AC-ACC-294
  - TC-AC-ACC-292
  - TC-AC-ACC-297
coverage:
  web: automated
---

# Tab Hardware: Screening Hardware List, Toolbar per Section, Badge, Kolom Photo, Panel Filter, dan Empty State

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): C-01 "PT Sejahtera Abadi" (Hardware List (Tabel A3 F7): HL-1 (Handheld Reader / RFID / Brand Alfa / HR-200 / SKU-HR-200 / Qty 12) dan HL-2 (Handheld Reader / RFID / Brand Beta / HB-1 / SKU `—` / Qty 3, BYO tanpa SKU); Quota dan Purchase History Hardware terisi), C-09 "PT Baru Daftar" (tanpa kuota/riwayat), C-FX19-1 "PT Nama Hardware Panjang" (Tabel A3; Active; Client Code `FX19-001`; Partner CV Mitra Sejati; Group Area Jakarta; FAMS Active; Hardware List satu baris: Category `Industrial Handheld Reader` (hierarki Handheld Devices > Industrial Handheld Reader), Type RFID, Brand `Brand Industri Nusantara Raya` (29 karakter), Model/Type `Model Handheld Seri Panjang 01` (30 karakter), Qty 2; dipakai TC-AC-ACC-292). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-290: Screening Tab Hardware

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `Hardware`
4. Verifikasi tab aktif `Hardware`
5. Verifikasi Hardware List (read-only) memiliki toolbar Search dengan placeholder "Search by category, brand, model, or SKU..." dan Filter
6. Verifikasi Hardware List berkolom `Photo (unsortable) | Category | Type | Brand | Model/Type | SKU | Qty`
7. Verifikasi Quota berkolom `Category | Type | Total Quota | Used | Available`
8. Verifikasi Purchase History Hardware memiliki toolbar Search dengan placeholder "Search by category, type, source, or action by...", Filter, dan Download
9. Verifikasi Purchase History Hardware berkolom `Category | Type | Qty | Source | Action by | Date`
10. Verifikasi Pagination tampil di footer

### TC-AC-ACC-468: Toolbar Section Hardware List (Search dan Filter) pada Tab Hardware

11. Lihat toolbar di atas tabel Hardware List dan Quota
12. Verifikasi toolbar Hardware List `Search | Filter` tanpa Download
13. Verifikasi toolbar Quota hanya `Download` (`Client-Hardware-PT Sejahtera Abadi`), tanpa Search dan Filter
14. Verifikasi toolbar Purchase History Hardware `Search | Filter | Download`

### TC-AC-ACC-291: Hardware List dikelompokkan per SKU atau per Device Name+Brand/Model untuk BYO tanpa SKU

15. Lihat Hardware List
16. Verifikasi baris Handheld Reader RFID Brand Alfa HR-200 SKU-HR-200 Qty 12
17. Verifikasi baris BYO Brand Beta HB-1 SKU `—` Qty 3

### TC-AC-ACC-295: Kolom Photo tidak sortable dan nilai kosong tampil —

18. Klik header Photo
19. Verifikasi tidak ada sort pada kolom Photo
20. Verifikasi foto kosong menampilkan `—`

### TC-AC-ACC-294: Screening Filter Hardware List: label, placeholder, dan field yang tidak ada

21. Klik Filter pada toolbar Hardware List
22. Verifikasi Category: dropdown multi-select searchable, placeholder "All categories"
23. Verifikasi Type: dropdown multi-select searchable, placeholder "All types"
24. Verifikasi Brand: dropdown multi-select searchable, placeholder "All brands"
25. Verifikasi Model/Type: dropdown multi-select searchable, placeholder "All models"
26. Verifikasi SKU, Qty, dan Photo tidak memiliki field filter
27. Verifikasi footer panel: `[Clear Field]` di kiri dan `[Apply]` di kanan
28. Klik ulang icon Filter untuk menutup panel Filter

### TC-AC-ACC-292: Badge Category (primary), Brand dan Model (dark) dengan truncate fixed-character dan hover

29. Kembali ke List lewat breadcrumb Client
30. Ganti isi Search dengan `PT Nama Hardware Panjang`, tekan Enter
31. Klik Company Name "PT Nama Hardware Panjang" untuk membuka Detail
32. Klik Tab `Hardware`
33. Lihat badge Category, Brand, dan Model dengan nama lebih dari 25 karakter pada Hardware List
34. Verifikasi badge Category tampil "Industrial H..dheld Reader"
35. Verifikasi badge Brand tampil "Brand Indust..santara Raya"
36. Verifikasi badge Model/Type tampil "Model Handhe..i Panjang 01"
37. Arahkan kursor ke badge Brand
38. Verifikasi tooltip badge Brand menampilkan "Brand Industri Nusantara Raya"
39. Arahkan kursor ke badge Model
40. Verifikasi tooltip badge Model menampilkan "Model Handheld Seri Panjang 01"
41. Arahkan kursor ke badge Category
42. Verifikasi tooltip badge Category menampilkan "Handheld Devices > Industrial Handheld Reader"

### TC-AC-ACC-297: Empty state Tab Hardware

43. Kembali ke List lewat breadcrumb Client
44. Ganti isi Search dengan `PT Baru Daftar`, tekan Enter
45. Klik Company Name "PT Baru Daftar" untuk membuka Detail
46. Klik Tab `Hardware`
47. Verifikasi Hardware List menampilkan "No hardware devices activated" dan "Active hardware devices will appear here."
48. Verifikasi Quota menampilkan "No hardware quota allocated" dan "Allocated hardware quotas will appear here."
49. Verifikasi Purchase History menampilkan "No purchase history yet" dan "Hardware quota purchase history will appear here."

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa pembacaan satu tab pada satu role, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna.
- Klik ulang icon Filter untuk menutup panel (D-001) adalah langkah penghubung (S-03). Absence pada TC-468 (tanpa Download, tanpa Search dan Filter) didahului Verifikasi toolbar yang sama sebagai anchor positif (bagian 8b butir 2).
- Urutan blok: TC-AC-ACC-292 ditempatkan setelah TC-AC-ACC-294 karena memakai Client C-FX19-1 (bukan C-01); TC-AC-ACC-295 dan 294 tetap membaca Hardware List C-01.
- Temuan untuk QA (S-15): TC-295 tidak menyebut baris yang berfoto kosong; kondisi foto kosong mengikuti seed C-01. Post Condition seluruh TC `-` sehingga tidak diasersi.
