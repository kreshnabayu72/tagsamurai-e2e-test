---
id: TC-GS-ACTLOG-E2E-035-setup-column-tab-user-action-pin-tiga-kolom-kolom-ke-4-dan-reset
title: "Setup Column Tab User Action: Pin Tiga Kolom, Kolom Ke-4, dan Reset"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-186
  - TC-GS-ACTLOG-187
  - TC-GS-ACTLOG-188
coverage:
  web: automated
---

# Setup Column Tab User Action: Pin Tiga Kolom, Kolom Ke-4, dan Reset

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > Activity Log > tab User Action.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis: Brand `Setup Column Brand {runId}-035` dibuat lewat API oleh Sari Dewi di hook `before` (aksi nyata yang menghasilkan baris log User Action, menjamin tabel tidak kosong). Cleanup di hook `after`: hapus Brand itu (entri Activity Log tidak bisa dihapus).
- Viewport: hook `before` mengatur lebar viewport sehingga tabel User Action dapat digulir horizontal (precondition TC-GS-ACTLOG-186 dan 187; nilai ditetapkan tim FE, usulan 1024 px) dan hook `after` memulihkannya ke ukuran awal.
- Kemampuan teknis: drag and drop baris kolom pada popup Setup Column; menggulir tabel secara horizontal; membaca kolom yang membeku dan urutannya dari kiri; membaca keadaan icon Pin (aktif atau nonaktif) dan tooltip saat hover; muat ulang halaman (F5) pada konteks browser yang sama supaya cache konfigurasi kolom tetap ada.
- Tabel "Kolom tabel User Action" (urutan default): `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`, `Modified By`.
- State global yang diubah: konfigurasi Setup Column tab User Action (urutan, visibilitas, pin) disimpan di cache browser per user dan terpisah per tab (PRD activity-log.md §4.1). Dipulihkan oleh langkah 10 (setelah TC-GS-ACTLOG-186) dan langkah 26 dan 29 (`[Reset to Default]`, `[Save]` pada TC-GS-ACTLOG-188); hook `after` sebagai cadangan memulihkan konfigurasi ke default lewat `[Reset to Default]` dan `[Save]` (atau menghapus cache konfigurasi kolom tab User Action).
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-GS-ACTLOG-186: Pin tiga kolom sekaligus dan urutan kolom beku

1. Klik header kolom `Column Visibility (⋯)`, klik `Setup Column...`
2. Klik icon Pin pada baris kolom `Date`, `Action`, `Object`
3. Seret kolom `Object` di atas `Date` di antara kolom beku
4. Klik `[Save]`
5. Gulir tabel ke kanan
6. Verifikasi ketiga kolom `Date`, `Action`, `Object` membeku di sisi kiri
7. Verifikasi urutan kolom beku dari kiri: `Object`, `Date`, `Action`
8. Verifikasi kolom lain ikut tergulir
9. Verifikasi kolom `Column Visibility (⋯)` tetap di sisi kanan

### Pemulihan state antar TC

10. Klik header kolom `Column Visibility (⋯)`, klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`
11. Tunggu aksi selesai (popup tertutup dan tombol aktif kembali)

### TC-GS-ACTLOG-187: Pin kolom ke-4 ditolak saat tiga kolom sudah beku

12. Klik header kolom `Column Visibility (⋯)`, klik `Setup Column...`
13. Klik icon Pin pada baris kolom `Date`, `Action`, `Object`
14. Verifikasi icon Pin kolom `Name` nonaktif (disabled)
15. Verifikasi icon Pin kolom `Name` tidak dapat diklik
16. Arahkan kursor ke icon Pin kolom `Name`
17. Verifikasi tooltip `"Maximum 3 columns can be pinned at once. Unpin another column first."` muncul
18. Verifikasi kolom `Name` tidak membeku
19. Klik icon Pin kolom `Date` untuk melepas pin
20. Verifikasi icon Pin kolom `Name` aktif kembali
21. Klik `(X)` pada header popup tanpa menyimpan

### Pemulihan state antar TC

22. Klik header kolom `Column Visibility (⋯)`, hilangkan centang kolom `Action`
23. Klik header kolom `Column Visibility (⋯)`, klik `Setup Column...`, klik icon Pin pada baris kolom `Date`, klik `[Save]`
24. Tunggu aksi selesai (popup tertutup dan tombol aktif kembali)

### TC-GS-ACTLOG-188: Reset to Default di Popup Setup Column

25. Klik header kolom `Column Visibility (⋯)`, klik `Setup Column...`
26. Klik `[Reset to Default]`
27. Verifikasi tabel di balik popup kembali ke susunan default: kolom `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`, `Modified By` tampil berurutan
28. Verifikasi tabel di balik popup tanpa kolom beku
29. Klik `[Save]`
30. Tunggu aksi selesai (popup tertutup dan tombol aktif kembali)
31. Muat ulang halaman (F5)
32. Verifikasi susunan default tetap berlaku setelah `[Save]` dan F5

## Notes

- Mode: FE+BE. Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan (TC-GS-ACTLOG-187 bergantung pada 186 dan 188 pada 183 menurut kolom Dependensi; 183 ada di spec 033).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10 dan 11 (mengembalikan konfigurasi ke default sebelum TC-GS-ACTLOG-187, karena langkah 4 menyimpan tiga kolom beku dan urutan baru), langkah 21 (menutup popup TC-GS-ACTLOG-187 tanpa menyimpan), langkah 22 sampai 24 (menyiapkan precondition TC-GS-ACTLOG-188: kolom `Action` disembunyikan lewat overlay dan kolom `Date` di-pin lewat popup; konfigurasi tersimpan sebelum `[Reset to Default]`), langkah 11, 24, dan 30 (tunggu aksi selesai sesudah `[Save]` yang hasilnya belum diasersi, sebelum membuka popup lagi atau memuat ulang halaman; 8b butir 8).
- Asersi tambahan di luar Expected TC: tidak ada.
- Pemisah dari spec 034: spec 034 mengulang drag dan pin per kolom untuk delapan kolom (sekitar 176 langkah dieksekusi), jauh di atas smell 35 langkah; spec ini mengubah pin tiga kolom, visibilitas, dan reset pada satu konfigurasi tersimpan, sehingga kegagalan keras pada iterasi 034 tidak boleh menutupi hasil spec ini.
- Pembagian TC: TC-GS-ACTLOG-180 sampai 183, 189, 190 ada di spec 033; TC-GS-ACTLOG-184 dan 185 ada di spec 034.
- Temuan untuk QA:
  - TC-GS-ACTLOG-187 Expected a menyebut tooltip `"Maximum 3 columns can be pinned at once. Unpin another column first."` pada icon Pin yang nonaktif; spec membaca tooltip dari hover. Elemen `disabled` bisa tidak menerima event hover pada sebagian implementasi; tim FE perlu memastikan tooltip dapat dibaca.
  - TC-GS-ACTLOG-187 tidak menyebut cara mengamati "kolom `Name` tidak membeku" di dalam popup (sebelum `[Save]`); spec mengamati status Pin kolom `Name` pada popup.
  - TC-GS-ACTLOG-188 precondition ("kolom `Action` disembunyikan, kolom `Date` di-pin") tidak menyebut cara menyiapkannya; spec menyiapkannya lewat overlay dan popup (langkah 22 dan 23).
  - TC-GS-ACTLOG-186 dan 187 tidak menyebut nilai lebar viewport yang membuat tabel dapat digulir; spec menyerahkan nilai ke tim FE (usulan 1024 px).
