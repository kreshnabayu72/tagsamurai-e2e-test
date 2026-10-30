---
id: TC-GS-ACTLOG-E2E-033-setup-column-tab-user-action-overlay-popup-sembunyikan-cancel-kolom-terakhir
title: "Setup Column Tab User Action: Overlay, Popup, Sembunyikan, Cancel, Kolom Terakhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-180
  - TC-GS-ACTLOG-181
  - TC-GS-ACTLOG-182
  - TC-GS-ACTLOG-183
  - TC-GS-ACTLOG-189
  - TC-GS-ACTLOG-190
coverage:
  web: automated
---

# Setup Column Tab User Action: Overlay, Popup, Sembunyikan, Cancel, Kolom Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > Activity Log > tab User Action.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis: Brand `Setup Column Brand {runId}-033` dibuat lewat API oleh Sari Dewi di hook `before` (aksi nyata yang menghasilkan baris log User Action, menjamin tabel tidak kosong sehingga pratinjau kolom teramati). Cleanup di hook `after`: hapus Brand itu (entri Activity Log tidak bisa dihapus).
- Kemampuan teknis: membaca keadaan checkbox (tercentang, aktif atau nonaktif) pada overlay dan popup; hover pada checkbox nonaktif untuk membaca tooltip; muat ulang halaman (F5) pada konteks browser yang sama supaya cache konfigurasi kolom tetap ada.
- Tabel "Kolom tabel User Action" (urutan default; parameter pengulangan langkah 40 sampai 49):

| Urutan | Kolom |
|---|---|
| 1 | `Date` |
| 2 | `Action` |
| 3 | `Object` |
| 4 | `Name` |
| 5 | `Field` |
| 6 | `Old Value` |
| 7 | `New Value` |
| 8 | `Modified By` |

- State global yang diubah: konfigurasi Setup Column tab User Action (visibilitas kolom) disimpan di cache browser per user dan terpisah per tab (PRD activity-log.md §4.1). Dipulihkan di langkah 38 dan oleh pengulangan langkah 40 sampai 49 (tiap kolom dicentang kembali); hook `after` sebagai cadangan memulihkan konfigurasi ke default lewat `[Reset to Default]` dan `[Save]` (atau menghapus cache konfigurasi kolom tab User Action).
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-GS-ACTLOG-180: Screening Overlay Column Visibility

1. Klik header kolom `Column Visibility (⋯)`
2. Verifikasi overlay memuat 8 kolom berurutan sesuai tabel "Kolom tabel User Action"
3. Verifikasi tiap kolom pada overlay punya checkbox tercentang
4. Verifikasi tiap kolom pada overlay punya checkbox aktif
5. Verifikasi tiap kolom pada overlay punya drag handle
6. Verifikasi item `Setup Column...` tampil di bagian bawah overlay

### TC-GS-ACTLOG-181: Screening Popup Setup Column

7. Klik item `Setup Column...`
8. Verifikasi header popup memuat judul `"Setup Column"`
9. Verifikasi header popup memuat tombol tutup `(X)`
10. Verifikasi body popup memuat 8 baris kolom berurutan sesuai tabel "Kolom tabel User Action"
11. Verifikasi tiap baris kolom punya checkbox tercentang
12. Verifikasi tiap baris kolom punya checkbox aktif
13. Verifikasi tiap baris kolom punya drag handle
14. Verifikasi tiap baris kolom punya icon Pin
15. Verifikasi tabel di balik popup tampil (siap menampilkan pratinjau)
16. Verifikasi footer popup memuat tombol `[Reset to Default]` dan `[Save]`

### TC-GS-ACTLOG-189: Cancel dan tombol tutup (X) membatalkan perubahan Popup Setup Column

17. Hilangkan centang kolom `Action` pada popup yang terbuka
18. Tekan `Esc`
19. Verifikasi popup tertutup
20. Verifikasi kolom `Action` tetap tampil di tabel
21. Klik header kolom `Column Visibility (⋯)`, klik `Setup Column...`, hilangkan centang kolom `Action`
22. Klik `(X)` pada header popup
23. Verifikasi popup tertutup
24. Verifikasi kolom `Action` tetap tampil di tabel

### TC-GS-ACTLOG-190: Kolom terakhir yang tampil tidak dapat disembunyikan

25. Klik header kolom `Column Visibility (⋯)`, klik `Setup Column...`
26. Hilangkan centang kolom `Date`, `Object`, `Name`, `Field`, `Old Value`, `New Value`, `Modified By` (tanpa klik `[Save]`)
27. Coba hilangkan centang kolom `Action`, arahkan kursor ke checkbox `Action`
28. Verifikasi checkbox kolom `Action` nonaktif (disabled)
29. Verifikasi checkbox kolom `Action` tidak dapat dihilangkan centangnya
30. Verifikasi tooltip `"At least one column must remain visible."` tampil
31. Centang kolom `Date`
32. Verifikasi checkbox kolom `Action` kembali aktif
33. Klik `(X)` pada header popup tanpa menyimpan

### TC-GS-ACTLOG-182: Overlay Column Visibility langsung menerapkan perubahan tanpa Save

34. Klik header kolom `Column Visibility (⋯)`, hilangkan centang kolom `Object`
35. Verifikasi kolom `Object` langsung hilang dari tabel tanpa klik tombol apa pun
36. Muat ulang halaman (F5)
37. Verifikasi kolom `Object` tetap tersembunyi setelah F5

### Pemulihan state antar TC

38. Klik header kolom `Column Visibility (⋯)`, centang kembali kolom `Object`

### TC-GS-ACTLOG-183: Sembunyikan dan tampilkan kolom lewat Popup Setup Column

39. Verifikasi seluruh 8 kolom tampil di tabel (keadaan awal sebelum pengulangan)
40. Untuk setiap baris tabel "Kolom tabel User Action" (langkah 40 sampai 49): klik header kolom `Column Visibility (⋯)`, klik `Setup Column...`
41. Hilangkan centang kolom pada kolom "Kolom" tabel itu
42. Verifikasi kolom itu hilang dari tabel di balik popup sebelum `[Save]`
43. Klik `[Save]`
44. Verifikasi kolom itu hilang dari tabel
45. Muat ulang halaman (F5)
46. Verifikasi kolom itu tetap tersembunyi setelah F5
47. Klik header kolom `Column Visibility (⋯)`, klik `Setup Column...`, centang kolom itu
48. Klik `[Save]`
49. Verifikasi kolom itu tampil kembali di tabel

## Notes

- Mode: FE+BE. Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-ACTLOG-180, 181, 189, 190, 182, 183. Alasan: 180 dan 181 hanya mengamati (screening di awal, bagian 3 konvensi); 189 dan 190 dibatalkan lewat `Esc`/`(X)` tanpa menyimpan, sehingga tidak mengubah konfigurasi tersimpan; 182 menyimpan perubahan (`Object` tersembunyi) sehingga dijalankan setelahnya dan dipulihkan sebelum 183; 183 menyimpan dan memulihkan tiap kolom di akhir.
- Alasan spec di atas smell 35 langkah: 49 langkah nominal, sekitar 119 langkah dieksekusi (langkah 40 sampai 49 diulang untuk delapan kolom). Semua blok satu topik (Setup Column Tab User Action), satu akun, tanpa dataset lain, tanpa kelas harness lain; keadaan konfigurasi dipulihkan di antara blok sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pengulangan: langkah 40 sampai 49 diulang untuk delapan baris tabel "Kolom tabel User Action"; tiap iterasi mengulang `Verifikasi` langkah 42, 44, 46, 49, sehingga tiap kolom (delapan) punya `Verifikasi` sendiri sesuai butir a sampai h Expected TC-GS-ACTLOG-183.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 26 dan 33 (menyiapkan precondition TC-GS-ACTLOG-190 di popup tanpa menyimpan: kolom selain `Action` disembunyikan; popup ditutup tanpa `[Save]`), langkah 38 (pemulihan kolom `Object`).
- Penghematan: langkah 17 memakai popup yang masih terbuka dari TC-GS-ACTLOG-181 (TC-GS-ACTLOG-189 langkah 1 berbunyi "Buka Popup Setup Column"), tanpa membuka ulang popup.
- Asersi tambahan di luar Expected TC, dengan alasan: langkah 39 (keadaan awal 8 kolom tampil sebagai anchor sebelum pengulangan TC-GS-ACTLOG-183, karena langkah 34 sampai 38 mengubah konfigurasi) dan langkah 44 (Expected a TC-GS-ACTLOG-183 menyebut "setelah `[Save]`" kolom hilang).
- Label tombol mengikuti `prd-conventions.md` §24.1: popup Setup Column tidak punya `[Cancel]`; langkah 16 mengasersi `[Reset to Default]` dan `[Save]` sebagai satu pasangan tombol footer, dan langkah 18 (`Esc`) menggantikan klik `[Cancel]` dari TC-GS-ACTLOG-189.
- Pembagian TC: TC-GS-ACTLOG-184 dan 185 ada di spec 034; TC-GS-ACTLOG-186, 187, 188 ada di spec 035.
- Temuan untuk QA:
  - TC-GS-ACTLOG-181 Expected c dan TC-GS-ACTLOG-189 menyebut tombol `[Cancel]` pada popup Setup Column; konvensi (§24.1 dan e2e-conventions §9) menyatakan popup tidak punya `[Cancel]` (footer `[Reset to Default]` dan `[Save]`). Spec mengikuti §24.1.
  - TC-GS-ACTLOG-190 precondition "kolom selain `Action` sudah disembunyikan" tidak menyebut apakah disimpan; spec menyembunyikannya di popup tanpa `[Save]`.
  - TC-GS-ACTLOG-181 Expected b "tabel di balik popup siap menampilkan pratinjau" tidak punya kriteria terukur; spec mengasersi tabel di balik popup tampil.
