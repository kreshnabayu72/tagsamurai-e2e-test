---
id: TC-AUTH-SES-E2E-011-confirm-cancel-duplicate-login-web
title: "Cancel, Escape, Backdrop, Klik Ganda Confirm, dan Confirm pada Dialog Duplicate Login Attempt di Web"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-29
  - TC-AUTH-SES-30
  - TC-AUTH-SES-31
  - TC-AUTH-SES-32
  - TC-AUTH-SES-26
  - TC-AUTH-SES-27
coverage:
  web: automated
---

# Cancel, Escape, Backdrop, Klik Ganda Confirm, dan Confirm pada Dialog Duplicate Login Attempt di Web

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): enam user profil BASE milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-29: `Irfan Utami` (`irfanutami+{runId}-011@qwertysystem.net`)
  - TC-AUTH-SES-30: `Tari Puspita` (`taripuspita+{runId}-011@qwertysystem.net`)
  - TC-AUTH-SES-31: `Budi Rahayu` (`budirahayu+{runId}-011@qwertysystem.net`)
  - TC-AUTH-SES-32: `Siti Anggraini` (`sitianggraini+{runId}-011@qwertysystem.net`)
  - TC-AUTH-SES-26: `Sari Ramadhan` (`sariramadhan+{runId}-011@qwertysystem.net`)
  - TC-AUTH-SES-27: `Galih Wulandari` (`galihwulandari+{runId}-011@qwertysystem.net`)
- Sesi web aktif di Browser A (Chrome on Windows, status Active) untuk tiap user dibuat di hook `before` lewat login API pada konteks Browser A masing-masing user sebagai kondisi yang di-seed BE.
- Browser B untuk tiap TC adalah konteks baru Firefox on macOS yang belum login; tiap TC memakai konteks Browser B sendiri.
- Hook `after`: akhiri semua sesi seed dan sesi yang dibuat spec, tutup konteks Browser A dan B, hapus keenam user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness c: multi-konteks):
  - dua konteks browser bersamaan dengan user agent yang dapat ditetapkan (Chrome on Windows, Firefox on macOS);
  - Browser A (sesi seed lewat login API) dapat dibuka pada Portal — Product Hub dengan koneksi SSE aktif untuk tiap user, dan menerima push SSE (Dialog "Logged Out") saat dibiarkan tanpa interaksi hingga 10 detik;
  - pengamatan state Loading pada [Confirm] di TC-AUTH-SES-32: bila state itu terlalu singkat untuk diamati, respons request Confirm ditahan sebentar lewat `Spectra.intercept()` (hanya menunda respons backend nyata, bukan memaksa kegagalan);
  - pembacaan data sesi platform per user (status Active, Force Logged Out, jumlah sesi) untuk asersi status sesi, disediakan tim FE/BE tanpa endpoint tertentu;
  - reCAPTCHA mode uji di environment (halaman Login with Password).
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) pada Browser A dan B.

## Test Steps

### TC-AUTH-SES-29: Cancel pada Dialog Duplicate Login Attempt menutup dialog dan sesi lama tetap aktif

1. Buka konteks Browser A baru (Chrome on Windows) dengan sesi seed milik `irfanutami+{runId}-011@qwertysystem.net`, lalu buka Portal — Product Hub supaya koneksi SSE aktif → halaman Portal — Product Hub tampil
2. Buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
3. Ketik email `irfanutami+{runId}-011@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul
4. Klik [Cancel]
5. Verifikasi Dialog tertutup di Browser B
6. Verifikasi Browser B kembali ke halaman Login
7. Verifikasi Tidak ada sesi baru di Browser B
8. Pindah ke Browser A dan klik area mana pun
9. Verifikasi Sesi di Browser A tetap Active
10. Verifikasi Browser A tidak menampilkan dialog apa pun

### TC-AUTH-SES-30: Tombol Escape pada Dialog Duplicate Login Attempt menutup dialog dengan efek Cancel

11. Buka konteks Browser A baru (Chrome on Windows) dengan sesi seed milik `taripuspita+{runId}-011@qwertysystem.net`, lalu buka Portal — Product Hub supaya koneksi SSE aktif → halaman Portal — Product Hub tampil
12. Tutup konteks Browser B TC sebelumnya (hapus sesi login browser), buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
13. Ketik email `taripuspita+{runId}-011@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul
14. Tekan tombol Escape
15. Verifikasi Dialog tertutup di Browser B
16. Verifikasi Browser B kembali ke halaman Login
17. Pindah ke Browser A (tanpa mengklik apa pun)
18. Verifikasi Sesi di Browser A tetap Active
19. Verifikasi Tidak ada sesi baru

### TC-AUTH-SES-31: Klik backdrop pada Dialog Duplicate Login Attempt menutup dialog dengan efek Cancel

20. Buka konteks Browser A baru (Chrome on Windows) dengan sesi seed milik `budirahayu+{runId}-011@qwertysystem.net`, lalu buka Portal — Product Hub supaya koneksi SSE aktif → halaman Portal — Product Hub tampil
21. Tutup konteks Browser B TC sebelumnya (hapus sesi login browser), buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
22. Ketik email `budirahayu+{runId}-011@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul
23. Klik area gelap di luar dialog
24. Verifikasi Dialog tertutup di Browser B
25. Verifikasi Browser B kembali ke halaman Login
26. Pindah ke Browser A (tanpa mengklik apa pun)
27. Verifikasi Sesi di Browser A tetap Active
28. Verifikasi Tidak ada sesi baru

### TC-AUTH-SES-32: Klik dua kali cepat pada [Confirm] hanya mengeksekusi satu kali

29. Buka konteks Browser A baru (Chrome on Windows) dengan sesi seed milik `sitianggraini+{runId}-011@qwertysystem.net`, lalu buka Portal — Product Hub supaya koneksi SSE aktif → halaman Portal — Product Hub tampil
30. Tutup konteks Browser B TC sebelumnya (hapus sesi login browser), buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
31. Ketik email `sitianggraini+{runId}-011@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul
32. Klik [Confirm] dua kali dengan cepat
33. Verifikasi Tombol [Confirm] berstatus Loading setelah klik pertama
34. Verifikasi Tombol [Confirm] disabled setelah klik pertama
35. Verifikasi Hanya satu sesi baru dibuat di Browser B
36. Verifikasi Browser B masuk Portal — Product Hub
37. Pindah ke Browser A (tanpa mengklik apa pun)
38. Verifikasi Sesi lama di Browser A berstatus Force Logged Out tepat satu kali

### TC-AUTH-SES-26: Confirm pada Dialog Duplicate Login Attempt mengaktifkan sesi baru dan meng-logout sesi lama

39. Buka konteks Browser A baru (Chrome on Windows) dengan sesi seed milik `sariramadhan+{runId}-011@qwertysystem.net`, lalu buka Portal — Product Hub supaya koneksi SSE aktif → halaman Portal — Product Hub tampil
40. Tutup konteks Browser B TC sebelumnya (hapus sesi login browser), buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
41. Ketik email `sariramadhan+{runId}-011@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul
42. Klik [Confirm]
43. Verifikasi Browser B masuk halaman Portal — Product Hub
44. Verifikasi Sesi web baru di Browser B berstatus Active
45. Verifikasi Tidak ada toast pada Browser B
46. Pindah ke Browser A dan amati tanpa interaksi selama 10 detik (event push SSE)
47. Verifikasi Sesi web lama di Browser A berstatus Force Logged Out
48. Verifikasi Dialog "Logged Out" tampil di Browser A

### TC-AUTH-SES-27: Klik OK pada Dialog Logged Out mengarahkan ke halaman Login

49. Buka konteks Browser A baru (Chrome on Windows) dengan sesi seed milik `galihwulandari+{runId}-011@qwertysystem.net`, lalu buka Portal — Product Hub supaya koneksi SSE aktif → halaman Portal — Product Hub tampil
50. Tutup konteks Browser B TC sebelumnya (hapus sesi login browser), buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
51. Ketik email `galihwulandari+{runId}-011@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul
52. Klik [Confirm] → Browser B masuk Portal — Product Hub
53. Pindah ke Browser A dan amati tanpa interaksi selama 10 detik (event push SSE) → Dialog "Logged Out" tampil
54. Di Browser A klik [OK]
55. Verifikasi Browser A diarahkan ke halaman Login with Password
56. Pindah ke Browser B
57. Verifikasi Sesi di Browser B tetap Active

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-29, 30, 31, 32, 26, lalu 27 (urutan TC sumber 26, 27, 29, 30, 31, 32). Jalur Cancel, Escape, dan backdrop (tanpa memutus sesi lama) diletakkan lebih dulu; TC-AUTH-SES-32 dan 26 yang meng-logout sesi lama menyusul; TC-AUTH-SES-27 (OK pada Dialog Logged Out) paling akhir. Tiap TC memakai user dan pasangan Browser A/B sendiri, jadi urutan tidak membuat TC saling bergantung.
- TC-AUTH-SES-26 dan 29 hingga 32 berdependensi pada TC-AUTH-SES-21 (login di Browser B hingga dialog muncul); TC-AUTH-SES-27 berdependensi pada TC-AUTH-SES-26 (Confirm hingga Dialog Logged Out tampil di Browser A). Langkah dependensi itu disalin utuh pada langkah 2-3, 12-13, 21-22, 30-31, 40-41, dan 50-53 (S-04). Asersi dialog Duplicate Login Attempt itu sendiri ada di `TC-AUTH-SES-E2E-001-screening-dialog-duplicate-login-dan-logged-out` dan `TC-AUTH-SES-E2E-009-limit-login-web-dan-duplicate-login`.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): menutup konteks Browser B TC sebelumnya (hapus sesi login browser) dan membuka konteks Browser B baru (langkah 12, 21, 30, 40, dan 50), serta berpindah antar Browser A dan B; membuka Browser A pada Portal — Product Hub di awal tiap TC (langkah 1, 11, 20, 29, 39, dan 49), karena Dialog "Logged Out" dan asersi "tanpa dialog apa pun" hanya bermakna bila Browser A hasil seeding API sedang membuka halaman app dengan koneksi SSE aktif.
- Pencatatan: asersi "tidak ada entri log baru" untuk Cancel (TC-AUTH-SES-29 Expected d) dan "tidak dicatat" (TC-AUTH-SES-30 dan 31 Expected b) tidak diasersikan di spec ini; dirujuk ke spec absence `TC-AUTH-SES-E2E-066-absence-duplicate-login-dan-session-expired` sesuai S-05.
- Temuan untuk QA: (1) TC-AUTH-SES-26 Post Condition b ("sesi-produk anak dari sesi lama ikut berakhir (jika ada)") bersyarat dan tidak ada sesi-produk pada user uji, sehingga tidak diasersikan; asersi sesi-produk ada di TC-AUTH-SES-255 (spec lain). (2) TC-AUTH-SES-32 Expected a meminta state Loading yang bersifat sesaat; spec mengamatinya dengan menahan sebentar respons Confirm bila perlu (Prerequisites). (3) TC-AUTH-SES-26, 29 hingga 32 menulis "password yang benar" tanpa menyebut reCAPTCHA atau nilai password; spec mengikuti TC dan memakai `Spectra.env.SES_PASSWORD`. (4) TC-AUTH-SES-27 memakai user dan sesi sendiri (`Galih Wulandari`) padahal dependensinya TC-AUTH-SES-26 memakai `Sari Ramadhan`; spec menyalin langkah dependensi untuk user TC-AUTH-SES-27. (5) TC-AUTH-SES-26 Expected c ("Dialog Logged Out tampil di Browser A") hanya merujuk TC-AUTH-SES-2 untuk isi dialog; spec mengasersi kemunculannya saja. (6) TC-AUTH-SES-26 b/c, 27, 29 c, 30, 31, dan 32 menyebut status sesi platform (Active, Force Logged Out) tanpa menyebut cara membacanya; spec memakai kemampuan pembacaan data sesi platform yang disediakan tim FE/BE (Prerequisites). (7) Precondition TC-AUTH-SES-26, 29, 30, 31, dan 32 hanya menyebut sesi web aktif di Browser A dan tidak menyatakan Browser A menampilkan Portal — Product Hub, padahal asersinya (Dialog "Logged Out", tanpa dialog, sesi tetap Active) bergantung pada halaman app yang terbuka; dependensi TC-AUTH-SES-21 (precondition b) mensyaratkannya. Spec menambah langkah penghubung membuka Portal — Product Hub di Browser A pada tiap TC.
- Ukuran: spec memuat sekitar 45 langkah di luar prefix login faktor-1 (melebihi sekitar 35) karena enam TC satu kelas harness (multi-konteks Browser A/B) berada dalam satu spec; tiap TC memakai user, sesi, dan pasangan Browser A/B sendiri, sehingga bagian berikutnya tetap bermakna meski TC lain di spec ini tidak dijalankan.
