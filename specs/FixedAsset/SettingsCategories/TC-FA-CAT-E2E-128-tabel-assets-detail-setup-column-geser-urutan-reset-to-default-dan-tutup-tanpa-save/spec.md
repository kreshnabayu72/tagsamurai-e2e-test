---
id: TC-FA-CAT-E2E-128-tabel-assets-detail-setup-column-geser-urutan-reset-to-default-dan-tutup-tanpa-save
title: "Tabel Assets pada Popup Detail: Geser Urutan Tujuh Kolom, Reset to Default, dan Penutupan Popup Setup Column Tanpa Save"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-549
  - TC-FA-CAT-551
  - TC-FA-CAT-552
coverage:
  web: automated
---

# Tabel Assets pada Popup Detail: Geser Urutan Tujuh Kolom, Reset to Default, dan Penutupan Popup Setup Column Tanpa Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 `Electronics` (Code `ELEC`) berisi `Laptop` (Code `ELEC-LT`, Total Asset 12); #21 (Asset Name `Laptop Dell`, `Laptop HP`); #22 (12 aset terhitung pada `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` (Model/Type `Latitude 5420`) dan `HP`; Group `Head Office > Floor 1 > Room 301`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia`, Model/Type `Elite Dragonfly G3 Notebook PC`, Group `Region Jawa > Jakarta Selatan Distribution Center`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`).
- Seed client Pre-setup dan aset (fixture backend, disediakan tim FE) mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Pre-setup #40 (label aset; dipakai bila kolom curated Label diuji) dan #56 (kolom Custom Field grup General yang Active) disediakan tim FE sebagai fixture backend; spec ini hanya membaca.
- Konfigurasi Setup Column yang disimpan spec ini dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (butir "Pemulihan Setup Column" di `suite.md`), bukan lewat `[Reset to Default]`.
- Parameter kolom pada TC-FA-CAT-549 (dipakai pada langkah perulangan):

| Baris | Kolom |
|---|---|
| 1 | `Name` |
| 2 | `Asset ID` |
| 3 | `Brand` |
| 4 | `Model/Type` |
| 5 | `Group` |
| 6 | `Status` |
| 7 | `Last Updated` |

## Test Steps
1. Klik node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
3. Klik header Actions (⋯) > `Setup Column...`

### TC-FA-CAT-549: Geser urutan kolom tabel Assets lewat popup dan persist

Untuk setiap baris pada tabel "Parameter kolom pada TC-FA-CAT-549" (langkah 4 sampai 5):

4. Geser kolom baris tabel ke posisi pertama pada daftar
5. Verifikasi preview menempatkan kolom baris tabel sebagai kolom data pertama
6. Klik `[Save]`
7. Tekan F5, klik node `Electronics` di Sidebar Category Tree, lalu klik elipsis (⋯) pada baris `Laptop` > `Detail`
8. Verifikasi urutan kolom data menjadi Last Updated, Status, Group, Model/Type, Brand, Asset ID, Name, TAG dan bertahan setelah F5

### TC-FA-CAT-551: Reset to Default tabel Assets mengembalikan konfigurasi bawaan setelah Save

9. Klik header Actions (⋯) > `Setup Column...`
10. Hilangkan centang kolom `Asset ID` dan geser kolom `Last Updated` ke posisi pertama
11. Klik `[Reset to Default]` lalu `[Save]`
12. Verifikasi preview dan tabel kembali ke kolom default berurutan Name, Asset ID, TAG, Brand, Model/Type, Group, Status, Last Updated
13. Tekan F5, klik node `Electronics` di Sidebar Category Tree, lalu klik elipsis (⋯) pada baris `Laptop` > `Detail`
14. Verifikasi konfigurasi default bertahan setelah F5

### TC-FA-CAT-552: Menutup popup Setup Column tabel Assets tanpa Save membuang perubahan preview

15. Klik header Actions (⋯) > `Setup Column...`
16. Hilangkan centang kolom `Asset ID` lalu klik icon close (✕)
17. Verifikasi tabel memakai konfigurasi tersimpan terakhir setelah ditutup lewat icon close (✕)
18. Klik header Actions (⋯) > `Setup Column...`
19. Ubah urutan kolom dengan menggeser `Last Updated` ke posisi pertama lalu tekan `Esc`
20. Verifikasi tabel memakai konfigurasi tersimpan terakhir setelah ditutup lewat `Esc`
21. Klik icon Close (✕) pada popup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Perulangan langkah 4 sampai 5 pada tujuh kolom (ekspansi 14 langkah, total 33 langkah dengan perulangan diekspansi, di bawah ambang 35) memakai parameter di tabel Prerequisites; tiap kolom diasersi setelah digeser (8b butir 7). Ketiga TC memakai popup Setup Column dari tabel Assets yang sama; urutan TC-FA-CAT-549 lalu 551 membuat konfigurasi tersimpan dibersihkan oleh Reset to Default sebelum TC-FA-CAT-552 (S-09).
- Expected TC-FA-CAT-549 butir a sampai g dipetakan ke Verifikasi langkah 5 pada tiap iterasi; butir h diasersi pada langkah sesudah F5 (7), bersama persistensinya.
- Langkah penghubung (S-03): langkah 7 dan langkah serupa pada TC-FA-CAT-551 membuka ulang popup karena F5 menutupnya; langkah terakhir menutup popup.
- Temuan untuk QA:
  - TC-FA-CAT-552 langkah 4 ("ubah urutan kolom") tidak menyebut kolom yang digeser; spec menggeser `Last Updated`.
  - TC-FA-CAT-549 butir h menyebut urutan hasil geser tanpa mengasersi Save sebelum F5; spec mengasersi urutan sesudah F5 saja (bertahan setelah Save dan F5).
