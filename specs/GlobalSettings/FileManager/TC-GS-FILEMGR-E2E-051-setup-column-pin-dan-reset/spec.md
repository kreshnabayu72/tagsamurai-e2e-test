---
id: TC-GS-FILEMGR-E2E-051-setup-column-pin-dan-reset
title: "Setup Column Tiga Surface: Pin, Unpin, Batas Tiga Pin, dan Reset to Default"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-183
  - TC-GS-FILEMGR-184
  - TC-GS-FILEMGR-185
coverage:
  web: automated
---

# Setup Column Tiga Surface: Pin, Unpin, Batas Tiga Pin, dan Reset to Default

## Prerequisites

- Mode: mock (spec hanya-FE, dijalankan tim FE sebagai integration test; API di-mock, tanpa backend nyata).
- Akun: Total Control Sinta Maharani (Tabel A1 TC) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`. Sesi login disuntikkan lewat seedSession di hook `before` tanpa memanggil backend, sehingga tidak ada password yang dipakai di spec ini.
- Kebutuhan mock (respons yang dipaksa):
  - Daftar file aktif tabel utama: `POST /v2/file-manager/{type}/files/list` (openapi baris 16); skema respons mengikuti openapi (baris 16). Mengembalikan 33 file Tabel A2 (ukuran halaman 10).
  - Daftar Recycle Bin: `POST /v2/file-manager/{type}/files/recycle-bin/list` (openapi baris 334); skema respons mengikuti openapi (baris 334). Mengembalikan 16 baris Tabel A3 (retensi 30 hari).
  - Daftar Changelog: `POST /v2/analytics-reporting/change-logs/list` (`low-level-design.md` baris 479; pembaca Changelog generik Analytics Reporting, tidak dideklarasikan di `openapi.yaml` modul); skema respons disediakan tim FE dari openapi Analytics Reporting (S-13). Mengembalikan 14 entri Tabel A4.
  - Stream SSE `client_{clientId}` (event `file.deleted` dan `file.purged`; `low-level-design.md` baris 429): di-mock tanpa event, tidak memancarkan event selama spec ini berjalan karena tidak ada langkah yang membutuhkannya.
  - Storage Usage: `GET /v2/file-manager/storage-usage` (openapi baris 579), hanya bila halaman memuatnya saat dibuka; skema respons mengikuti openapi (baris 579). Tidak menjadi objek langkah spec ini.
  - Respons preferensi Guided Tooltip untuk `guided_tooltip_seen_gs-file-manager`: true (di-mock). API pendukung di luar modul (identitas pengguna, sesi, menu, preferensi Guided Tooltip, General Settings) disediakan tim FE (S-13).
- Preferensi kolom (visibilitas, urutan, pin) tersimpan per tabel di browser (PRD File Manager; prd-conventions.md §9.3), bukan lewat API, sehingga tidak ada endpoint yang di-mock untuknya. "Tekan F5" dilakukan pada konteks browser yang sama supaya penyimpanan preferensi kolom tetap ada.
- Lebar konten ketiga tabel melebihi lebar viewport (overflow horizontal), karena TC-GS-FILEMGR-183 hanya bermakna bila scroll horizontal teramati. Kebutuhan lingkungan uji: viewport disempitkan atau data mock memaksa overflow; asersi tidak diubah (lihat Temuan untuk QA).
- Tabel "Surface yang diuji" (parameter langkah 1 sampai 12, 23 sampai 30, dan 31 sampai 42):

| Surface | Pembuka | Kolom (berurutan default) | Hide (langkah 26) | Drag ke posisi paling atas (langkah 27) | Pin (langkah 28) |
|---|---|---|---|---|---|
| Tabel utama | tanpa aksi (layar File Manager) | `File Name`, `File Format`, `User Name`, `Size`, `Uploaded By`, `Upload Date` | `Uploaded By` | `Upload Date` | `File Name` |
| Recycle Bin | klik tombol Recycle Bin di toolbar | `File Name`, `File Format`, `User Name`, `Size`, `Deleted Date`, `Deleted By`, `Auto-Purge In` | `Deleted By` | `Auto-Purge In` | `File Name` |
| Changelog | klik ikon Changelog di toolbar | `Date`, `Action`, `File Name`, `Field`, `Old Value`, `New Value`, `Modified By` | `Field` | `Modified By` | `Date` |

- Suite serial (`parallel: false`): konfigurasi kolom tiga tabel adalah state global browser yang dipakai spec lain.
- Respons preferensi Guided Tooltip untuk `guided_tooltip_seen_gs-file-manager`: true (di-mock), sehingga walkthrough tidak muncul otomatis; terdaftar di Kebutuhan mock.
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom ketiga tabel dikembalikan ke default (semua kolom tampil, urutan default, tanpa pin) lewat `[Reset to Default]` atau penghapusan penyimpanan preferensi kolom di browser; viewport dikembalikan ke ukuran awal.
- Kemampuan teknis: `Spectra.intercept()` untuk ketiga respons daftar; mengatur viewport; scroll horizontal tabel; drag and drop elemen daftar kolom; mengarahkan kursor ke ikon Pin disabled untuk membaca tooltip.

## Test Steps

### TC-GS-FILEMGR-183: Pin dan Unpin setiap kolom di popup Setup Column pada tiga surface

1. Untuk setiap surface pada tabel Prerequisites: buka surface sesuai kolom Pembuka, lakukan langkah 2 sampai 12 untuk setiap kolom pada kolom Kolom surface itu, lalu tutup modal bila surface berupa modal
2. Buka popup Setup Column lewat ikon (⋯) di header kolom Actions dan item `Setup Column...`
3. Klik ikon Pin kolom
4. Klik `[Save]`
5. Scroll tabel secara horizontal
6. Verifikasi kolom yang di-pin tetap di posisinya saat tabel di-scroll horizontal
7. Buka popup Setup Column
8. Klik ikon Pin kolom yang sama untuk Unpin
9. Klik `[Save]`
10. Scroll tabel secara horizontal
11. Verifikasi kolom ikut bergeser saat tabel di-scroll horizontal
12. Scroll tabel horizontal kembali ke posisi awal

### TC-GS-FILEMGR-184: Pin keempat dinonaktifkan saat tiga kolom sudah di-pin

13. Buka popup Setup Column tabel utama
14. Pin `File Name`
15. Pin `File Format`
16. Pin `User Name`
17. Arahkan kursor ke ikon Pin kolom `Size`
18. Verifikasi ikon Pin kolom lain (`Size`, `Uploaded By`, `Upload Date`) disabled dan tidak bisa diklik
19. Verifikasi tooltip ikon Pin disabled: "Maximum 3 columns can be pinned at once. Unpin another column first."
20. Unpin `User Name`
21. Verifikasi ikon Pin kolom lain (`Size`, `Uploaded By`, `Upload Date`) aktif kembali
22. Klik ikon close (X) untuk menutup popup tanpa Save

### TC-GS-FILEMGR-185: Reset to Default mengembalikan susunan kolom ke default lalu Save pada tiga surface

23. Untuk setiap surface pada tabel Prerequisites, lakukan langkah 24 sampai 30 (menyiapkan susunan yang sudah diubah dan disimpan, precondition TC)
24. Buka surface sesuai kolom Pembuka
25. Buka popup Setup Column
26. Hapus centang kolom pada "Hide"
27. Seret kolom pada "Drag ke posisi paling atas" ke posisi paling atas daftar
28. Pin kolom pada "Pin"
29. Klik `[Save]`
30. Tutup modal bila surface berupa modal
31. Untuk setiap surface pada tabel Prerequisites, lakukan langkah 32 sampai 42
32. Buka surface sesuai kolom Pembuka
33. Buka popup Setup Column
34. Klik `[Reset to Default]`
35. Verifikasi pratinjau menampilkan seluruh kolom sesuai urutan default kolom Kolom surface itu
36. Verifikasi pratinjau tanpa kolom yang di-pin
37. Klik `[Save]`
38. Verifikasi susunan default berlaku di tabel (urutan default, seluruh kolom tampil, tanpa pin)
39. Tekan F5
40. Buka kembali surface sesuai kolom Pembuka
41. Verifikasi susunan default bertahan setelah refresh
42. Tutup modal bila surface berupa modal

## Notes

- Mode: mock. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (183, 184, 185). TC-GS-FILEMGR-185 di akhir karena mengembalikan susunan ketiga tabel ke default sekaligus menjadi pemulihan state.
- Panjang spec: 42 langkah tertulis (sekitar 250 langkah setelah ekspansi 20 kolom pada TC-GS-FILEMGR-183), di atas sekitar 35 langkah. Alasan dipertahankan: seluruh blok satu kelas (Setup Column pin dan reset pada tiga tabel dengan komponen yang sama, Mode mock), langkah berulang memakai parameter di tabel Prerequisites tanpa langkah bersyarat (bagian 8b butir 7), dan setiap iterasi berdiri sendiri karena diakhiri Unpin dan scroll awal; kegagalan satu kolom tidak membuat iterasi lain kehilangan makna. Langkah yang diulang: 2 sampai 12 (20 iterasi: 6 + 7 + 7 kolom), 24 sampai 30 dan 32 sampai 42 (tiga iterasi).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 12 (mengembalikan posisi scroll), langkah 22 (menutup popup tanpa Save sehingga pin sementara tidak tersimpan), langkah 23 sampai 30 (menyiapkan precondition TC-GS-FILEMGR-185 "susunan kolom sudah diubah dan disimpan (hide, urut, pin)"; kolom yang diubah dipilih spec dan tercantum di tabel Prerequisites karena TC tidak menyebut kolom), langkah 30 dan 42 (menutup modal).
- Temuan untuk QA:
  - TC-GS-FILEMGR-183 tidak menyebut lebar viewport atau data yang membuat tabel overflow horizontal, padahal "scroll horizontal" hanya teramati bila konten melebihi lebar kontainer; lebar tabel dengan 6 sampai 7 kolom pada viewport desktop bisa tidak overflow. Dibutuhkan kemampuan viewport (mis. mempersempit) atau konfirmasi lebar minimum kolom.
  - TC-GS-FILEMGR-185 menyebut precondition "sudah diubah dan disimpan (hide, urut, pin)" tanpa kolom dan nilai konkret; spec memilih kolom sendiri (tabel Prerequisites) dan menyalin langkah penyiapan (S-04).
  - Endpoint baca Changelog tidak dideklarasikan di `openapi.yaml` modul File Manager (dilayani pembaca generik Analytics Reporting, `low-level-design.md` baris 479); skema responsnya berada di openapi Analytics Reporting dan disediakan tim FE (S-13).
