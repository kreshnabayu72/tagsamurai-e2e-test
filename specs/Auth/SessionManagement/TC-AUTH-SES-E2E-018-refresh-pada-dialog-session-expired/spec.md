---
id: TC-AUTH-SES-E2E-018-refresh-pada-dialog-session-expired
title: "Refresh pada Dialog Session Expired dan Browser Dibuka Ulang"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-50
  - TC-AUTH-SES-56
  - TC-AUTH-SES-57
  - TC-AUTH-SES-268
  - TC-AUTH-SES-58
  - TC-AUTH-SES-62
coverage:
  web: automated
---

# Refresh pada Dialog Session Expired dan Browser Dibuka Ulang

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): enam user profil BASE milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5 dan #11: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-62: `Siti Hidayat` (`sitihidayat+{runId}-018@qwertysystem.net`)
  - TC-AUTH-SES-50: `Citra Damayanti` (`citradamayanti+{runId}-018@qwertysystem.net`)
  - TC-AUTH-SES-58: `Nadia Santoso` (`nadiasantoso+{runId}-018@qwertysystem.net`)
  - TC-AUTH-SES-57: `Galih Setiawan` (`galihsetiawan+{runId}-018@qwertysystem.net`)
  - TC-AUTH-SES-56: `Sari Wijaya` (`sariwijaya+{runId}-018@qwertysystem.net`)
  - TC-AUTH-SES-268: `Budi Maulana` (`budimaulana+{runId}-018@qwertysystem.net`)
- Sesi web aktif (status Active) tiap user di Browser A dibuat lewat login API oleh langkah seeding di awal TC masing-masing, bukan di hook `before`: jam server uji dan jam browser/perangkat uji dimajukan kumulatif sehingga sesi yang dibuat lebih awal akan menua dan kedaluwarsa sebelum TC-nya berjalan.
- Hook `after`: akhiri semua sesi seed, tutup konteks Browser A, kembalikan jam server uji dan jam browser uji ke waktu nyata, hapus keenam user. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: time-travel dan penutupan browser): jam server uji dan jam browser/perangkat uji (timer idle dan Toast di client) dapat dimajukan bersama dengan presisi detik dan dipulihkan ke waktu nyata, sehingga spec ini tidak menunggu waktu nyata (selain pengamatan 10 detik pada TC-AUTH-SES-268); Browser A dapat ditutup sepenuhnya dan dibuka kembali dengan profil dan cookie persisten yang sama (TC-AUTH-SES-57, 56, 268; `AUTHSES-LOGIC-02i`); perekaman request jaringan pertama setelah browser dibuka kembali untuk status 401 (TC-AUTH-SES-56); deteksi dialog konfirmasi bawaan browser `beforeunload` (TC-AUTH-SES-58); emulasi tombol Escape dan klik di luar dialog (TC-AUTH-SES-62); pembacaan status sesi user uji dari sisi BE (TC-AUTH-SES-50, 57); reCAPTCHA mode uji di environment (halaman Login with Password).
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server uji dan jam browser/perangkat uji (diatur bersama), dipulihkan di hook `after`.
- Titik waktu: batas idle 15 menit; Dialog Session Expired pada idle 16 menit.
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) di Browser A.

## Test Steps

### TC-AUTH-SES-62: Dialog Session Expired web hanya menyediakan CTA Refresh dan tidak menyediakan opsi perpanjang sesi

1. Buka konteks Browser A baru lalu buat sesi web aktif `Siti Hidayat` lewat login API (seeding BE) → sesi berstatus Active
2. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
3. Biarkan Browser A tanpa aktivitas dan majukan jam server uji dan jam browser/perangkat uji bersama 10 menit → Toast Idle Warning tampil
4. Majukan jam server uji dan jam browser/perangkat uji bersama 6 menit lagi (idle 16 menit) → Dialog Session Expired tampil
5. Periksa seluruh dialog
6. Verifikasi Hanya tombol [Refresh] yang tersedia; tidak ada [Login] dan tidak ada opsi extend session
7. Tekan tombol Escape
8. Verifikasi Escape diabaikan dan dialog tetap tampil
9. Klik area gelap di luar dialog
10. Verifikasi Klik backdrop diabaikan dan dialog tetap tampil

### TC-AUTH-SES-50: Refresh pada Dialog Session Expired saat sesi masih expired mengarah ke Login with Password

11. Buka konteks Browser A baru lalu buat sesi web aktif `Citra Damayanti` lewat login API (seeding BE) → sesi berstatus Active
12. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
13. Biarkan Browser A tanpa aktivitas dan majukan jam server uji dan jam browser/perangkat uji bersama 10 menit → Toast Idle Warning tampil
14. Majukan jam server uji dan jam browser/perangkat uji bersama 6 menit lagi (idle 16 menit) → Dialog Session Expired tampil
15. Di Browser A klik [Refresh]
16. Verifikasi Browser A diarahkan ke halaman `Auth > Login with Password`
17. Verifikasi Tidak ada sesi baru

### TC-AUTH-SES-58: Idle tercapai saat user mengetik form menampilkan dialog dan data form tidak tersimpan

18. Buka konteks Browser A baru lalu buat sesi web aktif `Nadia Santoso` lewat login API (seeding BE) → sesi berstatus Active
19. Di Browser A buka `Global Settings > User` lalu buka Popup Create User → Popup Create User tampil
20. Isi sebagian field Popup Create User dengan teks `Draft Idle {runId}-018` tanpa Submit
21. Biarkan Browser A tanpa aktivitas dan majukan jam server uji dan jam browser/perangkat uji bersama 16 menit → Dialog Session Expired tampil
22. Klik [Refresh] → halaman Login with Password tampil
23. Verifikasi Navigasi dari [Refresh] tidak memicu konfirmasi bawaan browser (`beforeunload`)
24. Verifikasi User harus login ulang (halaman Login with Password tampil, tanpa sesi)
25. Ketik email `nadiasantoso+{runId}-018@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
26. Buka kembali `Global Settings > User` lalu buka Popup Create User yang sama → Popup Create User tampil
27. Verifikasi Data yang belum di-submit tidak tersimpan dan form kosong lagi

### TC-AUTH-SES-57: Menutup browser tidak mengakhiri sesi dan membuka ulang sebelum idle langsung masuk

28. Buka konteks Browser A baru lalu buat sesi web aktif `Galih Setiawan` lewat login API (seeding BE) → sesi berstatus Active
29. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
30. Tutup Browser A sepenuhnya (profil dan cookie persisten dipertahankan)
31. Majukan jam server uji dan jam browser/perangkat uji bersama 2 menit
32. Buka Browser A kembali dan buka alamat Portal — Product Hub
33. Verifikasi Browser A langsung masuk Portal — Product Hub tanpa login ulang
34. Verifikasi Sesi tetap berstatus Active
35. Verifikasi Idle timeout tetap berjalan selama browser tertutup (waktu kedaluwarsa sesi tidak diperpanjang oleh penutupan dan pembukaan browser)

### TC-AUTH-SES-56: Browser dibuka ulang setelah sesi kedaluwarsa langsung ke Login tanpa dialog dan tanpa toast

36. Buka konteks Browser A baru lalu buat sesi web aktif `Sari Wijaya` lewat login API (seeding BE) → sesi berstatus Active
37. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
38. Tutup Browser A sepenuhnya (profil dan cookie persisten dipertahankan)
39. Majukan jam server uji dan jam browser/perangkat uji bersama 16 menit
40. Buka Browser A kembali dan buka alamat Portal — Product Hub
41. Verifikasi Request pertama dijawab 401
42. Verifikasi Browser A langsung diarahkan ke halaman Login with Password
43. Verifikasi Dialog Session Expired, Toast Idle Warning, dan toast 401 global tidak tampil

### TC-AUTH-SES-268: Browser dibuka ulang setelah sesi kedaluwarsa tidak menampilkan toast 401 global

44. Buka konteks Browser A baru lalu buat sesi web aktif `Budi Maulana` lewat login API (seeding BE) → sesi berstatus Active
45. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
46. Tutup Browser A sepenuhnya (profil dan cookie persisten dipertahankan)
47. Majukan jam server uji dan jam browser/perangkat uji bersama 16 menit
48. Buka Browser A kembali dan buka alamat Portal — Product Hub
49. Amati halaman Login selama 10 detik
50. Verifikasi Browser A langsung ke halaman Login with Password
51. Verifikasi Tidak ada toast apa pun (tidak ada toast 401 global, tidak ada toast idle warning) dan tidak ada Dialog Session Expired

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness d (time-travel dan penutupan browser).
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-62, 50, 58, 57, 56, 268 (urutan TC sumber 50, 56, 57, 268, 58, 62). Pemeriksaan isi dialog tanpa aksi ditaruh paling awal, lalu [Refresh] ke Login, lalu skenario form, lalu tiga TC browser ditutup dan dibuka ulang. Tiap TC memakai user dan sesi sendiri sehingga urutan tidak membuat TC saling bergantung.
- Dependensi (S-04): TC-AUTH-SES-50 dan 62 berdependensi pada TC-AUTH-SES-46 (idle sampai Dialog Session Expired); langkah penyiapan 1 dan 2 TC-AUTH-SES-46 disalin sebagai langkah 3-4, 13-14 (asersi Toast, Dialog, dan halaman beku TC-AUTH-SES-46 diuji di spec `TC-AUTH-SES-E2E-016-idle-timeout-dan-toast-warning-web`). TC-AUTH-SES-268 berdependensi pada TC-AUTH-SES-56; langkah tutup browser, majukan 16 menit, dan buka kembali disalin sebagai langkah 46-48.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): membuka konteks Browser A baru dan membuat sesi seed; membuka Portal — Product Hub; membuka `Global Settings > User` dan Popup Create User; menutup dan membuka kembali Browser A; mengamati halaman Login 10 detik.
- Pembagian TC lintas spec: TC-AUTH-SES-49 (Refresh pada Dialog Session Expired saat sesi sudah valid, dua tab) ada di spec `TC-AUTH-SES-E2E-019-session-expired-multi-tab`. Expected butir c TC-AUTH-SES-49 (tidak ada entri log baru) adalah asersi absence dan ada di spec absence `TC-AUTH-SES-E2E-066-absence-duplicate-login-dan-session-expired` (S-05).
- Temuan untuk QA: (1) TC-AUTH-SES-58 menyebut "isi sebagian field form" dan "Popup Create User" tanpa menyebut field, nilai, atau izin user BASE untuk membuka Create User; spec mengisi teks `Draft Idle {runId}-018` pada satu field dan mengikuti TC untuk izin aksesnya. (2) TC-AUTH-SES-57 Expected b "idle timeout tetap berjalan selama browser tertutup" tidak menyebut cara mengamatinya; spec menuliskannya sebagai satu `Verifikasi` dan cara amatnya diputuskan di tahap script. (3) TC-AUTH-SES-50 Expected b "tidak ada sesi baru" dan TC-AUTH-SES-57 Expected b "sesi tetap Active" butuh pembacaan status sesi dari sisi BE yang tidak punya endpoint di OpenAPI modul; kebutuhan ditulis di Prerequisites. (4) TC-AUTH-SES-56 Precondition b menyebut sesi sudah kedaluwarsa saat browser ditutup, sedangkan Langkah Uji memajukan jam server 16 menit setelah menutup browser; spec mengikuti Langkah Uji. (5) TC-AUTH-SES-56 dan 268 hampir sama (268 menambah pengamatan 10 detik tanpa toast); keduanya tetap dipertahankan sebagai TC terpisah dengan user terpisah. (6) TC-AUTH-SES-58 langkah 3 dan 4 menyebut login ulang tanpa merinci kredensial dan reCAPTCHA; spec memakai email dan password user uji dan mengandalkan reCAPTCHA mode uji. (7) TC-AUTH-SES-50 memuat "tidak ada pencatatan" atau "tidak ada sesi baru" sebagai Expected; pengecekannya mengikuti Notes pembagian TC di atas.
- Ukuran: spec memuat 51 langkah (melebihi sekitar 35) karena enam TC satu kelas harness (time-travel dan penutupan browser) berada dalam satu spec; tiap TC memakai user dan sesi sendiri yang dibuat di awal TC-nya, sehingga bagian berikutnya tetap bermakna meski TC lain di spec ini tidak dijalankan.
