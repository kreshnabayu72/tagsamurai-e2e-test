---
id: TC-GS-BRAND-E2E-070-resilience-tulis-create-edit-timeout-dan-toast
title: "Resilience Tulis Brand: Create Gagal 5xx, Timeout lalu Retry, Edit Gagal 5xx, dan Durasi Toast"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-BRAND-66
  - TC-GS-BRAND-67
  - TC-GS-BRAND-89
  - TC-GS-BRAND-253
coverage:
  web: automated
---

# Resilience Tulis Brand: Create Gagal 5xx, Timeout lalu Retry, Edit Gagal 5xx, dan Durasi Toast

## Prerequisites

- Mode: FE+BE dengan intercept parsial di atas backend nyata (bagian 6 konvensi).
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Master Reference > Brand.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (tetap di environment, tidak berubah karena Edit dipaksa gagal, tanpa suffix `{runId}`): `Orion Tech` (bebas relasi).
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi):
  - `Ivy Co {runId}-070` (D-34): dibuat sukses pada TC-GS-BRAND-253.
  - `Jade Co {runId}-070` dan `Xenon Co {runId}-070`: input yang submit-nya dipaksa gagal (tidak membuat data).
  - `Yarrow Co {runId}-070` (D-14): tersimpan oleh percobaan pertama TC-GS-BRAND-67 (respons ditahan tetapi request sampai ke server, lihat kebutuhan intercept), sehingga percobaan kedua ditolak dan tepat satu baris ada.
  - `Orion Q`: input Edit yang dipaksa gagal.
- Kebutuhan intercept (`Spectra.intercept()`), semuanya pada request ke endpoint Brand dan dilepas setelah dipakai:
  - respons Create Brand dipaksa HTTP 500;
  - respons Create Brand pertama dipaksa timeout: respons ditahan melewati batas klien sedangkan request tetap diteruskan ke server (server menyimpan brand), lalu intercept dilepas untuk memulihkan jaringan;
  - respons Edit Brand dipaksa HTTP 500.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): lepaskan semua intercept; hapus lewat API `Ivy Co {runId}-070`, `Yarrow Co {runId}-070`, dan sisa `Jade Co`, `Xenon Co` bersuffix `{runId}-070` bila ada.
- Tidak ada state global lain yang diubah.
- TC-GS-BRAND-66, 67, 89, 253: login sebagai Total Control dan berada di Global Settings > Master Reference > Brand.

## Test Steps

### TC-GS-BRAND-253: Toast sukses hilang otomatis ±4 detik, toast error persisten

1. Klik [+ Brand], isi Brand Name `Ivy Co {runId}-070`, klik [Submit]
2. Verifikasi toast sukses "Success, brand has been created." tampil di kanan bawah
3. Amati toast sukses selama 6 detik
4. Verifikasi toast sukses hilang otomatis ±4 detik (sudah tidak tampil pada detik ke-6)
5. Paksa respons Create Brand HTTP 500 (intercept)
6. Klik [+ Brand], isi Brand Name `Jade Co {runId}-070`, klik [Submit]
7. Verifikasi toast error "Error, failed to create brand." tampil di kanan bawah
8. Amati toast error selama 10 detik
9. Verifikasi toast error tetap tampil setelah 10 detik
10. Tutup toast error secara manual
11. Verifikasi toast error hilang setelah ditutup

### TC-GS-BRAND-66: Create gagal 5xx mempertahankan form

12. Pada form Create yang masih terbuka (intercept 500 masih aktif), kosongkan Brand Name lalu isi `Xenon Co {runId}-070`
13. Klik [Submit]
14. Verifikasi toast error: "Error, failed to create brand."
15. Verifikasi form tetap terbuka
16. Verifikasi `Xenon Co {runId}-070` dipertahankan di field Brand Name
17. Verifikasi [Submit] enabled kembali
18. Klik `✕` pada form Create
19. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
20. Klik `[Leave]`
21. Search `Xenon Co {runId}-070` pada tabel Brand
22. Verifikasi `Xenon Co {runId}-070` tidak ada di tabel

### TC-GS-BRAND-67: Create timeout lalu retry tidak menghasilkan duplikat

23. Lepas intercept 500, paksa timeout pada respons Create Brand pertama (intercept)
24. Klik [+ Brand], isi Brand Name `Yarrow Co {runId}-070`, klik [Submit]
25. Verifikasi percobaan pertama: toast error "Error, failed to create brand."
26. Verifikasi form tetap terbuka
27. Pulihkan jaringan (lepas intercept timeout), klik [Submit] lagi
28. Verifikasi percobaan kedua ditolak dengan pesan `Brand Name already exists`
29. Klik `✕` pada form Create
30. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
31. Klik `[Leave]`
32. Search `Yarrow Co {runId}-070`
33. Verifikasi pencarian `Yarrow Co {runId}-070` menampilkan tepat 1 baris

### TC-GS-BRAND-89: Edit gagal 5xx mempertahankan form

34. Search `Orion Tech` (menggantikan Search sebelumnya), paksa respons Edit Brand HTTP 500 (intercept)
35. Klik `⋯` pada baris Orion Tech > Edit, ubah Brand Name menjadi `Orion Q`
36. Klik [Save]
37. Verifikasi toast error: "Error, failed to update brand."
38. Verifikasi form tetap terbuka dengan `Orion Q`
39. Verifikasi [Save] enabled
40. Klik `✕` pada form Edit
41. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
42. Klik `[Leave]`
43. Verifikasi tabel tetap menampilkan Orion Tech

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`. Kelas fault injection (prinsip 13b) dengan intercept parsial di atas backend nyata; kegagalan dipicu dengan `Spectra.intercept()` pada request browser, sehingga bukan `Mode: mock`.
- Urutan TC di spec berbeda dari urutan sumber (253, 66, 67, 89): TC-GS-BRAND-253 memuat langkah sukses dahulu (tanpa intercept) lalu intercept 500 sehingga form dengan intercept 500 yang sama dipakai ulang oleh TC-GS-BRAND-66 (prinsip 3.6/3.8, hemat buka form); lalu TC-GS-BRAND-67 (timeout) dan TC-GS-BRAND-89 (Edit).
- TC-GS-BRAND-66 Langkah Uji 2 ("Klik [+ Brand]") tidak ditulis ulang karena form dari TC-GS-BRAND-253 langkah 6 masih terbuka (hemat buka form, prinsip 6); nilai diganti ke `Xenon Co {runId}-070` sesuai Data Uji TC.
- Temuan untuk QA: TC-GS-BRAND-67 Expected Result b mengizinkan dua hasil (percobaan kedua sukses atau ditolak `Brand Name already exists`). Spec menetapkan cabang ditolak (langkah 28) karena mekanisme timeout di Prerequisites meneruskan request pertama ke server sehingga brand sudah tersimpan; Expected Result c (tepat 1 baris, langkah 33) tetap penentu. Kebutuhan mekanisme timeout itu sudah dicatat di Prerequisites.
- TC-GS-BRAND-67 berstatus `Manual Only` di TC sumber; sesuai bagian 2 konvensi, hambatan teknis bukan alasan mengeluarkan TC, dan kebutuhan intercept dicatat di Prerequisites.
- Wording timeout pada TC-GS-BRAND-67 mengikuti toast "Error, failed to create brand." dan form tetap terbuka (Expected Result a TC sumber).
- Langkah penghubung: langkah 18 sampai 20, 29 sampai 31, dan 40 sampai 42 (menutup form dirty lewat `✕`, dialog `Unsaved Changes`, dan `[Leave]`, sebagai pembersihan state antar TC; verifikasi dialog pada langkah 19, 30, dan 41 adalah asersi tambahan yang tidak ada di TC, ditulis agar penutupan form deterministik, konvensi bagian 10 S-08), langkah 23 dan 34 (melepas atau memasang intercept), serta langkah 21, 32, dan 34 (Search nama brand yang diasersikan atau yang menjadi target baris, supaya baris berada di tabel yang terlihat).
- Urutan dalam TC-GS-BRAND-253: Verifikasi toast tampil (langkah 2 dan 7) dijalankan segera setelah aksi, sebelum langkah Amati (langkah 3 dan 8); langkah 4 dan 9 memverifikasi keadaan toast sesudah jendela amatan.
- Alasan spec tidak dipecah (43 langkah): satu kelas harness (fault injection dengan intercept parsial), satu set data, dan form Create yang terbuka dipakai ulang antara TC-GS-BRAND-253 dan 66 (prinsip 6); bagian sesudah tiap TC (67 dan 89) tetap bermakna berdiri sendiri, tetapi memecah akan mengulang pemasangan intercept dan pembukaan form.
