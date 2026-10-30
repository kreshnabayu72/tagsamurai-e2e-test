---
id: TC-GS-FILEMGR-E2E-050-setup-column-hide-reorder-isolasi-dan-persistensi
title: "Setup Column Tiga Surface: Hide, Reorder, Isolasi Antar Tabel, dan Persistensi setelah Refresh dan Logout"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-181
  - TC-GS-FILEMGR-182
  - TC-GS-FILEMGR-188
  - TC-GS-FILEMGR-189
coverage:
  web: automated
---

# Setup Column Tiga Surface: Hide, Reorder, Isolasi Antar Tabel, dan Persistensi setelah Refresh dan Logout

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sinta Maharani (Tabel A1 TC) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi. Langkah 36 dan 37 (logout lalu login kembali akun yang sama) diwajibkan TC-GS-FILEMGR-189.
- Data Pre-setup: Tabel A2 (33 file aktif), Tabel A3 (16 baris Recycle Bin, retensi 30 hari), dan Tabel A4 (14 entri Changelog). Dataset disiapkan lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme dan endpoint seeding tidak didefinisikan di TC, lihat Temuan untuk QA). Spec hanya membaca data; tidak ada aksi tulis ke data dan tidak ada data dinamis. Preferensi kolom tersimpan per tabel di browser (PRD File Manager; prd-conventions.md §9.3).
- Tabel "Surface yang diuji" (parameter langkah 1 sampai 10 dan 11 sampai 21):

| Surface | Pembuka | Kolom (berurutan) | Posisi kolom pertama setelah diseret ke atas |
|---|---|---|---|
| Tabel utama | tanpa aksi (layar File Manager) | `File Name`, `File Format`, `User Name`, `Size`, `Uploaded By`, `Upload Date` | kolom data pertama setelah Checkbox |
| Recycle Bin | klik tombol Recycle Bin di toolbar | `File Name`, `File Format`, `User Name`, `Size`, `Deleted Date`, `Deleted By`, `Auto-Purge In` | kolom data pertama setelah Checkbox |
| Changelog | klik ikon Changelog di toolbar | `Date`, `Action`, `File Name`, `Field`, `Old Value`, `New Value`, `Modified By` | kolom pertama |

- Susunan kolom tiga tabel default (semua kolom tampil, urutan default, tanpa pin) saat spec dimulai.
- Suite serial (`parallel: false`): konfigurasi kolom tiga tabel adalah state global browser dan dataset (33 file aktif, 16 baris Recycle Bin, 14 entri Changelog) tidak boleh berubah bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom ketiga tabel dikembalikan ke default lewat `[Reset to Default]` atau penghapusan penyimpanan preferensi kolom di browser.
- Kemampuan teknis: drag and drop elemen daftar kolom; membaca urutan kolom tabel dan pratinjau popup; logout dan login pada browser yang sama (penyimpanan preferensi kolom di browser tidak dihapus oleh logout).

## Test Steps

### TC-GS-FILEMGR-181: Centang dan hapus centang setiap kolom di popup Setup Column pada tiga surface

1. Untuk setiap surface pada tabel Prerequisites: buka surface sesuai kolom Pembuka, lakukan langkah 2 sampai 10 untuk setiap kolom pada kolom Kolom surface itu, lalu tutup modal bila surface berupa modal
2. Buka popup Setup Column lewat ikon (⋯) di header kolom Actions dan item `Setup Column...`
3. Hapus centang kolom
4. Verifikasi pratinjau popup tidak lagi menampilkan kolom
5. Klik `[Save]`
6. Verifikasi kolom hilang dari tabel
7. Buka popup Setup Column
8. Centang kembali kolom
9. Klik `[Save]`
10. Verifikasi kolom muncul kembali di tabel pada posisi semula

### TC-GS-FILEMGR-182: Mengubah urutan setiap kolom lewat drag di popup Setup Column pada tiga surface

11. Untuk setiap surface pada tabel Prerequisites: buka surface sesuai kolom Pembuka, lakukan langkah 12 sampai 21 untuk setiap kolom pada kolom Kolom surface itu, lalu tutup modal bila surface berupa modal
12. Buka popup Setup Column
13. Seret kolom ke posisi paling atas daftar
14. Klik `[Save]`
15. Verifikasi kolom menjadi kolom pertama di tabel sesuai kolom "Posisi kolom pertama setelah diseret ke atas"
16. Tekan F5
17. Buka kembali surface sesuai kolom Pembuka
18. Verifikasi urutan baru bertahan setelah refresh halaman (kolom masih menjadi kolom pertama)
19. Buka popup Setup Column
20. Klik `[Reset to Default]`
21. Klik `[Save]`

### TC-GS-FILEMGR-188: Perubahan Setup Column satu tabel tidak memengaruhi tabel lain

22. Sembunyikan kolom `Size` tabel utama lewat overlay Column Visibility (⋯)
23. Verifikasi tabel utama tanpa kolom `Size`
24. Klik tombol Recycle Bin di toolbar
25. Verifikasi Recycle Bin masih menampilkan kolom `Size`
26. Tutup modal Recycle Bin
27. Klik ikon Changelog di toolbar
28. Verifikasi Changelog masih menampilkan ketujuh kolom: `Date`, `Action`, `File Name`, `Field`, `Old Value`, `New Value`, `Modified By`
29. Tutup modal Changelog
30. Tampilkan kembali kolom `Size` tabel utama lewat overlay Column Visibility (⋯)

### TC-GS-FILEMGR-189: Konfigurasi Setup Column tersimpan setelah refresh dan setelah logout lalu login

31. Buka popup Setup Column tabel utama
32. Hapus centang `Uploaded By`
33. Klik `[Save]`
34. Tekan F5
35. Verifikasi kolom `Uploaded By` tetap tidak tampil
36. Logout
37. Login kembali sebagai Sinta Maharani di browser yang sama (kredensial `Spectra.env.GS_TC_PASSWORD`)
38. Buka layar Global Settings > File Manager
39. Verifikasi kolom `Uploaded By` tetap tidak tampil
40. Buka popup Setup Column tabel utama
41. Centang kembali `Uploaded By`
42. Klik `[Save]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (181, 182, 188, 189). TC-GS-FILEMGR-182 diakhiri `[Reset to Default]` lalu `[Save]` sehingga susunan default berlaku untuk TC-GS-FILEMGR-188, yang mensyaratkan susunan default.
- Panjang spec: 42 langkah tertulis (sekitar 380 langkah setelah ekspansi 20 kolom pada TC-GS-FILEMGR-181 dan 182), di atas sekitar 35 langkah. Alasan dipertahankan: seluruh blok satu kelas (Setup Column pada tiga tabel dengan komponen yang sama), langkah berulang memakai parameter di tabel Prerequisites tanpa langkah bersyarat (bagian 8b butir 7), dan setiap iterasi kolom berdiri sendiri karena diakhiri pemulihan ke posisi semula atau default; kegagalan satu kolom tidak membuat iterasi lain kehilangan makna. Langkah yang diulang: 2 sampai 10 (20 iterasi: 6 + 7 + 7 kolom), 12 sampai 21 (20 iterasi).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 17 (membuka kembali surface setelah F5 supaya langkah 18 bisa diamati), langkah 19 sampai 21 (kembali ke default sebelum kolom berikutnya, mengikuti TC-GS-FILEMGR-182 langkah 1 dan Data Uji), langkah 26 dan 29 (menutup modal), langkah 30 dan 40 sampai 42 (memulihkan kolom yang disembunyikan; hook `after` sebagai cadangan), langkah 38 (membuka File Manager setelah login ulang).
- Langkah 16 sampai 18 menambahkan observasi refresh untuk Expected d TC-GS-FILEMGR-182 per iterasi; Langkah TC sumber tidak memuat refresh (lihat Temuan untuk QA).
- Langkah 36 dan 37 adalah logout dan login ulang akun yang sama sebagaimana diwajibkan TC-GS-FILEMGR-189 langkah 3; bukan ganti akun.
- Temuan untuk QA:
  - TC-GS-FILEMGR-182 Expected d ("Urutan baru bertahan setelah refresh halaman sebelum Reset to Default") tidak memiliki langkah refresh di kolom Langkah Uji; spec menambahkan F5 per iterasi (langkah 16 sampai 18) sebagai observasi.
  - Mekanisme dan endpoint seeding Tabel A2, A3, dan A4 tidak didefinisikan di TC (Q-4); hitungan dan susunan kolom mengasumsikan dataset di-seed ulang per spec dan suite serial (Q-7).
  - TC-GS-FILEMGR-189 menyatakan persistensi "di browser yang sama" setelah logout; spec mengandalkan penyimpanan preferensi kolom di browser (PRD File Manager; prd-conventions.md §9.3) tanpa mengarang endpoint.
