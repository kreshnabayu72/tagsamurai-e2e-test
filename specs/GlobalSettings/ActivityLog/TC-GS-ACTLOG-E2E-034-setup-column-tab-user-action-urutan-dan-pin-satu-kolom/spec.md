---
id: TC-GS-ACTLOG-E2E-034-setup-column-tab-user-action-urutan-dan-pin-satu-kolom
title: "Setup Column Tab User Action: Urutan dan Pin Satu Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-184
  - TC-GS-ACTLOG-185
coverage:
  web: automated
---

# Setup Column Tab User Action: Urutan dan Pin Satu Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > Activity Log > tab User Action.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis: Brand `Setup Column Brand {runId}-034` dibuat lewat API oleh Sari Dewi di hook `before` (aksi nyata yang menghasilkan baris log User Action, menjamin tabel tidak kosong). Cleanup di hook `after`: hapus Brand itu (entri Activity Log tidak bisa dihapus).
- Viewport: hook `before` mengatur lebar viewport sehingga tabel User Action dapat digulir horizontal (precondition TC-GS-ACTLOG-185; nilai ditetapkan tim FE, usulan 1024 px) dan hook `after` memulihkannya ke ukuran awal.
- Kemampuan teknis: drag and drop baris kolom pada popup Setup Column; menggulir tabel secara horizontal; membaca kolom yang membeku (posisi tetap saat tabel digulir); muat ulang halaman (F5) pada konteks browser yang sama supaya cache konfigurasi kolom tetap ada.
- Tabel "Kolom tabel User Action" (urutan default; parameter pengulangan langkah 1 sampai 10 dan 11 sampai 22):

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

- State global yang diubah: konfigurasi Setup Column tab User Action (urutan dan pin) disimpan di cache browser per user dan terpisah per tab (PRD activity-log.md §4.1). Dipulihkan oleh langkah 8 dan 9 (`[Reset to Default]`, `[Save]`) dan langkah 18 sampai 20 (Unpin) pada tiap iterasi; hook `after` sebagai cadangan memulihkan konfigurasi ke default lewat `[Reset to Default]` dan `[Save]` (atau menghapus cache konfigurasi kolom tab User Action).
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-GS-ACTLOG-184: Geser urutan kolom lewat Popup Setup Column

1. Untuk setiap baris tabel "Kolom tabel User Action" (langkah 1 sampai 10): klik header kolom `Column Visibility (⋯)`, klik `Setup Column...`
2. Seret baris kolom pada kolom "Kolom" tabel itu ke posisi paling atas pada popup
3. Verifikasi kolom itu menjadi kolom pertama di tabel di balik popup
4. Klik `[Save]`
5. Verifikasi kolom itu menjadi kolom pertama di tabel
6. Muat ulang halaman (F5)
7. Verifikasi urutan tetap setelah `[Save]` dan F5 (kolom itu kolom pertama)
8. Klik header kolom `Column Visibility (⋯)`, klik `Setup Column...`, klik `[Reset to Default]`
9. Klik `[Save]`
10. Verifikasi urutan kolom kembali ke default sesuai tabel "Kolom tabel User Action"

### TC-GS-ACTLOG-185: Pin dan Unpin satu kolom lewat Popup Setup Column

11. Untuk setiap baris tabel "Kolom tabel User Action" (langkah 11 sampai 22): klik header kolom `Column Visibility (⋯)`, klik `Setup Column...`
12. Klik icon Pin pada baris kolom pada kolom "Kolom" tabel itu
13. Klik `[Save]`
14. Gulir tabel ke kanan
15. Verifikasi kolom itu membeku di sisi kiri saat tabel digulir horizontal
16. Muat ulang halaman (F5), gulir tabel ke kanan
17. Verifikasi kolom itu tetap membeku di sisi kiri setelah F5
18. Klik header kolom `Column Visibility (⋯)`, klik `Setup Column...`
19. Klik icon Pin pada baris kolom itu lagi
20. Klik `[Save]`
21. Gulir tabel ke kanan
22. Verifikasi kolom itu ikut tergulir (tidak membeku) setelah Unpin

## Notes

- Mode: FE+BE. Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan (TC-GS-ACTLOG-185 bergantung pada 181 menurut kolom Dependensi; 181 ada di spec 033).
- Alasan spec di atas smell 35 langkah: 22 langkah nominal, sekitar 176 langkah dieksekusi (langkah 1 sampai 10 dan 11 sampai 22 masing-masing diulang untuk delapan kolom). Semua iterasi satu topik (Setup Column Tab User Action), satu akun, satu dataset, tanpa kelas harness lain; konfigurasi dikembalikan ke default pada akhir tiap iterasi sehingga kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Pemisah dari spec 035: gabungan 034 dan 035 sekitar 208 langkah dieksekusi, jauh di atas smell 35 langkah; spec 035 mengubah pin tiga kolom, visibilitas, dan reset dalam satu konfigurasi tersimpan, sehingga kegagalan keras pada salah satu dari 16 iterasi di sini tidak boleh menutupi hasil 035.
- Pengulangan: langkah 1 sampai 10 dan langkah 11 sampai 22 diulang untuk delapan baris tabel "Kolom tabel User Action"; tiap iterasi mengulang `Verifikasi` langkah 3, 5, 7, 10 dan 15, 17, 22, sehingga tiap kolom (delapan) punya `Verifikasi` sendiri.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 14, 16, 21 (menggulir tabel sebelum asersi pin; langkah 16 menggulir ulang setelah F5 karena posisi gulir tidak bertahan). Langkah 8 dan 9 (`[Reset to Default]` dan `[Save]`) adalah langkah 2 TC-GS-ACTLOG-184, bukan penghubung.
- Langkah 18 sampai 20 (Unpin) mengembalikan konfigurasi pin ke default pada tiap iterasi; Unpin adalah bagian TC (langkah 2 TC-GS-ACTLOG-185).
- Asersi tambahan di luar Expected TC, dengan alasan: langkah 3 dan 5 memecah Expected a TC-GS-ACTLOG-184 ("kolom menjadi kolom pertama di tabel" saat di balik popup dan sesudah `[Save]`), langkah 10 memuat Expected "setelah reset urutan kembali ke default".
- Pembagian TC: TC-GS-ACTLOG-180 sampai 183, 189, 190 ada di spec 033; TC-GS-ACTLOG-186 sampai 188 ada di spec 035.
- Temuan untuk QA:
  - TC-GS-ACTLOG-184 untuk kolom `Date` menyeret kolom ke "posisi paling atas", padahal `Date` sudah kolom pertama pada urutan default; asersi "menjadi kolom pertama" lolos tanpa perubahan nyata dan tidak membuktikan perilaku drag untuk kolom itu.
  - TC-GS-ACTLOG-185 tidak menyebut nilai lebar viewport yang membuat tabel dapat digulir; spec menyerahkan nilai ke tim FE (usulan 1024 px).
  - TC-GS-ACTLOG-185 Expected tidak menyebut apakah posisi gulir bertahan setelah F5; spec menggulir ulang sebelum asersi.
