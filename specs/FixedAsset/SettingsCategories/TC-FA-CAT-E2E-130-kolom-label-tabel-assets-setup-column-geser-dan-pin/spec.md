---
id: TC-FA-CAT-E2E-130-kolom-label-tabel-assets-setup-column-geser-dan-pin
title: "Kolom Curated Label pada Tabel Assets: Default Tersembunyi, Ceklis, Geser Urutan, dan Pin dengan Persist"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-555
  - TC-FA-CAT-556
  - TC-FA-CAT-557
coverage:
  web: automated
---

# Kolom Curated Label pada Tabel Assets: Default Tersembunyi, Ceklis, Geser Urutan, dan Pin dengan Persist

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 `Electronics` (Code `ELEC`) berisi `Laptop` (Code `ELEC-LT`, Total Asset 12); #21 (Asset Name `Laptop Dell`, `Laptop HP`); #22 (12 aset terhitung pada `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` (Model/Type `Latitude 5420`) dan `HP`; Group `Head Office > Floor 1 > Room 301`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia`, Model/Type `Elite Dragonfly G3 Notebook PC`, Group `Region Jawa > Jakarta Selatan Distribution Center`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`).
- Seed client Pre-setup dan aset (fixture backend, disediakan tim FE) mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Label aset (Pre-setup #40, dibuat di Settings > Asset Master > Labels, disediakan tim FE): `Laptop Dell - 1` label `Fragile`; `Laptop Dell - 2` label `Fragile` dan `Priority`; `Laptop Dell - 3` label `Fragile`, `Priority`, `Insured`, dan `Outdoor`; `Laptop HP - 1` label `Bulky`; aset lain tanpa label (termasuk `Laptop Dell - 4`).
- Konfigurasi Setup Column yang disimpan spec ini dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (butir "Pemulihan Setup Column" di `suite.md`).
- Lebar viewport diatur cukup sempit sehingga tabel Assets pada popup Detail dapat di-scroll horizontal (langkah 1); tanpa itu asersi Pin kolom `Label` tetap di kiri saat scroll (langkah 23 dan 25) tidak bermakna.

## Test Steps
1. Atur lebar viewport sehingga tabel Assets pada popup Detail dapat di-scroll horizontal
2. Klik node `Electronics` di Sidebar Category Tree
3. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-555: Setup Column kolom curated Label, default tersembunyi, ceklis menampilkan, Save dan persist

4. Verifikasi kolom `Label` tidak ada di tabel
5. Klik header Actions (⋯) > `Setup Column...`
6. Verifikasi checkbox kolom `Label` ☐ unchecked tetapi enabled
7. Centang kolom `Label`
8. Verifikasi Live Preview langsung menambahkan kolom `Label`
9. Klik `[Save]`
10. Verifikasi tabel memuat kolom `Label` setelah Save
11. Tekan F5, klik node `Electronics` di Sidebar Category Tree, lalu klik elipsis (⋯) pada baris `Laptop` > `Detail`
12. Verifikasi kolom `Label` tetap tampil setelah F5

### TC-FA-CAT-556: Geser kolom curated Label lewat popup dan persist

13. Klik header Actions (⋯) > `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`
14. Klik header Actions (⋯) > `Setup Column...`, centang kolom `Label`, lalu klik `[Save]`
15. Klik header Actions (⋯) > `Setup Column...`, geser `Label` ke posisi pertama, lalu klik `[Save]`
16. Verifikasi kolom `Label` menjadi kolom data pertama pada preview dan tabel
17. Tekan F5, klik node `Electronics` di Sidebar Category Tree, lalu klik elipsis (⋯) pada baris `Laptop` > `Detail`
18. Verifikasi urutan kolom `Label` sebagai kolom data pertama bertahan setelah F5

### TC-FA-CAT-557: Pin kolom curated Label dan persist

19. Klik header Actions (⋯) > `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`
20. Klik header Actions (⋯) > `Setup Column...`, centang kolom `Label`, lalu klik `[Save]`
21. Klik header Actions (⋯) > `Setup Column...`, klik icon Pin pada `Label`, lalu klik `[Save]`
22. Scroll tabel horizontal
23. Verifikasi kolom `Label` tetap di kiri saat scroll horizontal
24. Tekan F5, klik node `Electronics` di Sidebar Category Tree, klik elipsis (⋯) pada baris `Laptop` > `Detail`, lalu scroll tabel horizontal
25. Verifikasi Pin bertahan setelah F5: kolom `Label` tetap di kiri saat scroll horizontal
26. Klik icon Close (✕) pada popup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Langkah penghubung (S-03/S-09/S-11, tanpa `Verifikasi`): langkah 1 mengatur viewport; `[Reset to Default]` lalu `[Save]` sebelum TC-FA-CAT-556 dan TC-FA-CAT-557 mengembalikan kolom `Label` ke default tersembunyi agar ceklis TC berikutnya tidak membalik keadaan, serta penutupan popup di akhir. Reset to Default hanya dipakai sebagai langkah penghubung di antara TC; pemulihan akhir lewat hook `after`.
- Expected TC-FA-CAT-555 butir a dipecah menjadi dua Verifikasi (kolom tidak ada, checkbox unchecked tetapi enabled) dan butir b menjadi dua (Live Preview, setelah Save).
- Temuan untuk QA:
  - TC-FA-CAT-556 menyimpan dua kali (ceklis lalu geser); spec mengikuti dua Save tersebut.
  - TC-FA-CAT-555 mengamati kolom di tabel sebelum Setup Column dibuka; spec mengamati tabel lebih dulu sebelum membuka popup.
