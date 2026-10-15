---
id: TC-AUTH-SES-E2E-067-absence-sesi-produk-dan-concurrent
title: "Absence Pencatatan Sesi-produk dan Concurrent: Reuse, Limit Reached, dan End Product Berulang"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-101
  - TC-AUTH-SES-102
  - TC-AUTH-SES-104
  - TC-AUTH-SES-204
  - TC-AUTH-SES-263
coverage:
  web: automated
  mobile: automated
---

# Absence Pencatatan Sesi-produk dan Concurrent: Reuse, Limit Reached, dan End Product Berulang

## Prerequisites

- Mode: FE+BE (TC-AUTH-SES-263 memakai intercept parsial di atas backend nyata).
- Kelas harness g (asersi absence) dengan harness multi-konteks (web dan mobile pada user yang sama, TC-AUTH-SES-104) dan failure injection (TC-AUTH-SES-263). Client Q2 (Tabel Data Uji Pre-setup #12): subscription Fixed Asset dan Supply Asset Active, kuota masing-masing 2.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tujuh user profil BASE milik Client Q2 dengan App Access Fixed Asset dan Supply Asset (user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - Seed seat (Tabel Data Uji Pre-setup #7): `Gunawan Prakoso` (`gunawanprakoso+{runId}-067@qwertysystem.net`) dan `Melati Anggun` (`melatianggun+{runId}-067@qwertysystem.net`), masing-masing dengan sesi platform web Active yang dibuat lewat API di awal bagian TC yang memakainya (bukan di hook `before`)
  - TC-AUTH-SES-204: `Galih Pratama` (`galihpratama+{runId}-067@qwertysystem.net`)
  - TC-AUTH-SES-102: `Dimas Firmansyah` (`dimasfirmansyah+{runId}-067@qwertysystem.net`)
  - TC-AUTH-SES-101: `Lestari Saputra` (`lestarisaputra+{runId}-067@qwertysystem.net`)
  - TC-AUTH-SES-104: `Eko Rahayu` (`ekorahayu+{runId}-067@qwertysystem.net`)
  - TC-AUTH-SES-263: `Sari Puspita` (`saripuspita+{runId}-067@qwertysystem.net`)
- Sesi platform web Active untuk kelima user TC di Browser A (Chrome on Windows, konteks browser terpisah per TC) dibuat di awal bagian TC masing-masing lewat login API (langkah penghubung), bukan di hook `before`, karena batas idle 15 menit berjalan selama spec berlangsung; Browser A berada di Portal — Product Hub. Sesi mobile Active milik `Eko Rahayu` di perangkat Android uji A (Tabel Data Uji Pre-setup #10) dibuat lewat login nyata di perangkat A dengan [Not now] pada Prompt Enable Biometric pada awal bagian TC-AUTH-SES-104 (data aplikasi akun sebelumnya dibersihkan).
- Kondisi seat dan sesi-produk per TC disiapkan lewat API oleh akun aktor pada awal bagian TC itu (langkah penghubung), bukan di hook `before`, karena kuota Client Q2 hanya 2 dan tiap TC membutuhkan jumlah seat terpakai yang berbeda: sebelum menyiapkan, semua sesi-produk Fixed Asset dan Supply Asset aktif Client Q2 diakhiri lewat API. Sesi-produk awal yang dibuat lewat API pada langkah penghubung tercatat sebelum langkah pembuka bagian itu dan tidak dihitung sebagai entri "baru" atau "kedua".
- Konteks browser (hook `before`): Browser Admin login oleh akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26), dipakai membaca `Global Settings > Activity Log > Session`, `Activity Log > Session` milik Fixed Asset, dan `Global Settings > User > Detail > User Log`.
- Hook `after`: matikan failure injection; akhiri semua sesi dan sesi-produk seed (web, mobile, dan dua seed seat); bersihkan data aplikasi mobile di perangkat Android uji A; tutup semua konteks browser; hapus ketujuh user. Hook tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- State global yang diubah: seat Fixed Asset Client Q2 (diisi penuh oleh seed pada TC-AUTH-SES-204 dan 102, diambil dan dilepas pada TC lain) dan failure injection 5xx pada request End Product (TC-AUTH-SES-263, `POST /v2/iam/auth/product-sessions/{id}/end`, sumber: `auth/session-management/API/openapi.yaml`). Pemulihan di hook `after`; suite berjalan serial.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: banyak konteks browser bersamaan; reload (F5) dan tab baru pada Browser A; navigasi langsung ke URL dashboard Fixed Asset; satu perangkat Android uji A dengan aplikasi mobile terpasang dan dapat diketuk oleh driver otomasi, serta login nyata di aplikasi mobile dengan [Not now] pada Prompt Enable Biometric (TC-AUTH-SES-104); failure injection 5xx pada request End Product lewat `Spectra.intercept()`, dinyalakan dan dimatikan oleh langkah (TC-AUTH-SES-263); pembacaan stempel waktu entri log untuk membedakan entri baru dari entri yang dibuat sebelum langkah pembuka bagian; akses akun aktor ke `Activity Log > Session` milik Fixed Asset (surface produk, PRD §8 surface #2).
- Akun yang dipakai: user uji masing-masing TC pada Browser A dan perangkat Android uji A; akun aktor Total Control (Global Settings) pada Browser Admin.

## Test Steps

### TC-AUTH-SES-204 (bagian absence, Concurrent limit reached tidak pernah muncul di GS Session): Popup limit tampil saat seat penuh

1. Siapkan lewat API: buat sesi web Active milik `Galih Pratama` di Browser A, akhiri semua sesi-produk aktif Client Q2, lalu buat satu sesi-produk Fixed Asset Active milik `Gunawan Prakoso` dan satu milik `Melati Anggun` sehingga seat terpakai 2 dari kuota 2
2. Di Browser A buka Portal — Product Hub sebagai `galihpratama+{runId}-067@qwertysystem.net` → halaman Portal — Product Hub tampil
3. Di Browser A klik card Fixed Asset di Portal — Product Hub → Popup "Concurrent session limit reached" tampil
4. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Galih Pratama` yang dibuat sesudah langkah 3 dimulai
5. Verifikasi Tidak ada entri `Concurrent limit reached` untuk `Galih Pratama` di `Global Settings > Activity Log > Session`

### TC-AUTH-SES-102 (bagian absence, tidak ada log baru): Pemegang seat yang reload saat seat sama dengan limit

6. Tutup konteks Browser A TC sebelumnya (hapus sesi login browser) dan buka konteks Browser A baru; siapkan lewat API: buat sesi web Active milik `Dimas Firmansyah` di Browser A, akhiri semua sesi-produk aktif Client Q2, lalu buat satu sesi-produk Fixed Asset Active milik `Dimas Firmansyah` dan satu milik `Gunawan Prakoso` sehingga seat terpakai 2 sama dengan kuota 2
7. Di Browser A buka Portal — Product Hub sebagai `dimasfirmansyah+{runId}-067@qwertysystem.net` → halaman Portal — Product Hub tampil
8. Di Browser A buka dashboard Fixed Asset → dashboard Fixed Asset tampil
9. Tekan F5 untuk reload → dashboard Fixed Asset tampil
10. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Dimas Firmansyah` yang dibuat sesudah langkah 8 dimulai
11. Verifikasi Tidak ada entri baru untuk `Dimas Firmansyah` di `Global Settings > Activity Log > Session` untuk kondisi reload oleh pemegang seat saat seat sama dengan limit
12. Buka `Activity Log > Session` milik Fixed Asset dan cari entri untuk `Dimas Firmansyah` yang dibuat sesudah langkah 8 dimulai
13. Verifikasi Tidak ada entri baru untuk `Dimas Firmansyah` di `Activity Log > Session` milik Fixed Asset untuk kondisi reload oleh pemegang seat saat seat sama dengan limit
14. Buka `Global Settings > User > Detail > User Log` milik `Dimas Firmansyah` dan cari entri yang dibuat sesudah langkah 8 dimulai
15. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi reload oleh pemegang seat saat seat sama dengan limit

### TC-AUTH-SES-101 (bagian absence, tanpa entri Session started kedua): Reload dan tab baru pada produk yang sama

16. Tutup konteks Browser A TC sebelumnya (hapus sesi login browser) dan buka konteks Browser A baru; siapkan lewat API: buat sesi web Active milik `Lestari Saputra` di Browser A, akhiri semua sesi-produk aktif Client Q2, lalu buat satu sesi-produk Fixed Asset Active milik `Lestari Saputra` (seat terpakai 1 dari kuota 2)
17. Di Browser A buka Portal — Product Hub sebagai `lestarisaputra+{runId}-067@qwertysystem.net` → halaman Portal — Product Hub tampil
18. Di Browser A buka dashboard Fixed Asset → dashboard Fixed Asset tampil
19. Tekan F5 untuk reload → dashboard Fixed Asset tampil
20. Buka tab baru di Browser A dan buka URL dashboard Fixed Asset yang sama → dashboard Fixed Asset tampil
21. Pindah ke Browser Admin, buka `Activity Log > Session` milik Fixed Asset, dan cari entri `Session started` untuk `Lestari Saputra` yang dibuat sesudah langkah 18 dimulai
22. Verifikasi Tidak ada entri `Session started` kedua untuk `Lestari Saputra` di `Activity Log > Session` milik Fixed Asset
23. Buka `Global Settings > User > Detail > User Log` milik `Lestari Saputra` dan cari entri `Session started (Fixed Asset)` yang dibuat sesudah langkah 18 dimulai
24. Verifikasi Tidak ada entri `Session started (Fixed Asset)` kedua di `Global Settings > User > Detail > User Log`

### TC-AUTH-SES-104 (bagian absence, tanpa entri Session started kedua): Produk dibuka dari mobile setelah dibuka dari web

25. Tutup konteks Browser A TC sebelumnya (hapus sesi login browser) dan buka konteks Browser A baru; siapkan lewat API: akhiri semua sesi-produk aktif Client Q2; sesi web Active milik `Eko Rahayu` di Browser A (Chrome on Windows) dan sesi-produk Fixed Asset Active milik `Eko Rahayu` yang dibuat dari web (seat terpakai 1)
26. Di perangkat Android uji A bersihkan data aplikasi akun sebelumnya, lalu login dengan `ekorahayu+{runId}-067@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, ketuk [Not now] pada Prompt Enable Biometric → app masuk Portal — Product Hub (sesi mobile aktif di perangkat A)
27. Di perangkat Android uji A buka aplikasi mobile dan buka card Fixed Asset → Fixed Asset terbuka
28. Pindah ke Browser Admin, buka `Activity Log > Session` milik Fixed Asset, dan cari entri `Session started` untuk `Eko Rahayu` yang dibuat sesudah langkah 27 dimulai
29. Verifikasi Tidak ada entri `Session started` kedua untuk `Eko Rahayu` di `Activity Log > Session` milik Fixed Asset
30. Buka `Global Settings > User > Detail > User Log` milik `Eko Rahayu` dan cari entri `Session started (Fixed Asset)` yang dibuat sesudah langkah 27 dimulai
31. Verifikasi Tidak ada entri `Session started (Fixed Asset)` kedua di `Global Settings > User > Detail > User Log`

### TC-AUTH-SES-263 (bagian absence, tidak mencatat Session ended kedua): End Product berulang pada sesi-produk yang sudah Ended

32. Tutup konteks Browser A TC sebelumnya (hapus sesi login browser) dan buka konteks Browser A baru; siapkan lewat API: sesi web Active milik `Sari Puspita` di Browser A dan sesi-produk Fixed Asset Active milik `Sari Puspita` (seat terpakai); Browser A berada di dashboard Fixed Asset sebagai `saripuspita+{runId}-067@qwertysystem.net`
33. Aktifkan failure injection 5xx pada request End Product → request End Product dijawab 500
34. Di Browser A klik App Switcher di header Fixed Asset saat failure injection aktif
35. Nonaktifkan failure injection → request End Product kembali normal
36. Di Browser A klik App Switcher lagi
37. Di Browser A klik App Switcher sekali lagi pada sesi-produk yang sudah Ended
38. Pindah ke Browser Admin, buka `Global Settings > User > Detail > User Log` milik `Sari Puspita`, dan cari entri `Session ended (Fixed Asset)` yang dibuat sesudah langkah 36 dimulai
39. Verifikasi Tidak ada entri `Session ended (Fixed Asset)` kedua di `Global Settings > User > Detail > User Log`: hanya satu entri untuk sesi-produk itu
40. Verifikasi Tidak ada entri `Session ended (Fixed Asset)` di `Global Settings > User > Detail > User Log` yang dibuat sesudah langkah 37 dimulai

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pembagian TC lintas spec (prinsip 10): spec ini hanya memuat klausa absence dari lima TC; asersi fungsional (popup, dialog, status sesi-produk, seat, toast) dan asersi pencatatan (presence) tetap di spec asal dan tidak diulang di sini. Spec asal: TC-AUTH-SES-101 dan 102 di `TC-AUTH-SES-E2E-031-buka-produk-seat-tersedia-dan-reuse-sesi-produk`; TC-AUTH-SES-104 di `TC-AUTH-SES-E2E-034-sesi-produk-bersama-web-dan-mobile`; TC-AUTH-SES-263 di `TC-AUTH-SES-E2E-033-cascade-sesi-produk-dan-pelepasan-seat`; TC-AUTH-SES-204 di `TC-AUTH-SES-E2E-058-pencatatan-produk-concurrent-dan-cascade` (asersi presence `Concurrent limit reached` di `Activity Log > Session` milik Fixed Asset dan User Log). Spec absence lain ada di `TC-AUTH-SES-E2E-060-absence-pencatatan-sesi`.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini 204, 102, 101, 104, 263 (urutan TC sumber 101, 102, 104, 204, 263). TC-AUTH-SES-204 dan 102 membutuhkan seat Fixed Asset Client Q2 penuh sehingga dikelompokkan di awal; TC-AUTH-SES-104 memakai perangkat mobile dan ditaruh sesudah TC web; TC-AUTH-SES-263 mengakhiri sesi-produk miliknya sendiri dan ditaruh paling akhir. Tiap TC memakai user sendiri dan menyiapkan kondisi seat di awal bagiannya sehingga tidak saling bergantung (S-06).
- Langkah dependensi disalin (S-04): TC-AUTH-SES-204 dari TC-AUTH-SES-96 (langkah 1 sampai 3: seat penuh oleh dua seed, buka Portal sebagai user TC, klik card Fixed Asset hingga popup tampil); TC-AUTH-SES-263 dari TC-AUTH-SES-132 (langkah 36 dan 37: klik App Switcher di header Fixed Asset). Asersi hasil langkah dependensi (popup, status sesi-produk, seat) diuji di spec pemilik TC.
- Spec ini memuat 40 langkah karena lima TC absence masing-masing menyiapkan seat dan sesinya sendiri di awal bagian; tiap TC berdiri sendiri sehingga tidak dipecah.
- Penentuan entri "baru": TC sumber tidak menyebut baris log awal sebagai anchor. Entri yang dihitung hanya yang dibuat sesudah langkah pembuka bagian itu menurut stempel waktu (langkah 3, 8, 18, 27, dan 36 untuk TC-AUTH-SES-263); entri yang dibuat oleh pembuatan sesi-produk awal pada langkah penghubung berada sebelum batas itu. Pada TC-AUTH-SES-263 entri `Session ended (Fixed Asset)` dari klik kedua (langkah 36) adalah satu-satunya yang diharapkan; yang diasersi absen adalah entri kedua.
- Surface log: TC-AUTH-SES-204 menyebut GS Session, sehingga dibaca di `Global Settings > Activity Log > Session`. TC-AUTH-SES-101 menyebut Session Fixed Asset dan User Log; TC-AUTH-SES-102 dan 104 tidak menyebut surface. Surface produk `Activity Log > Session` milik Fixed Asset adalah forward-dependency (Catatan modul, NC-15, PRD §12 #3) dan bertanda `[DEFERRED]` pada dependensi TC-AUTH-SES-204 dan 132. Karena itu TC-AUTH-SES-263 dibaca hanya di User Log (Global Settings); TC-AUTH-SES-101, 102, dan 104 tetap membaca surface Fixed Asset di samping User Log mengikuti spec pencatatan `TC-AUTH-SES-E2E-058`, dan pembacaan User Log tetap berlaku bila surface Fixed Asset belum tersedia.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): menutup konteks Browser A TC sebelumnya dan membuka konteks baru (S-09); menyiapkan seat, sesi, dan sesi-produk lewat API; membuka Portal sebagai user TC; perpindahan antar konteks (Browser Admin, Browser A, perangkat Android uji A); membuka halaman log; menyalakan dan mematikan failure injection (langkah 33 dan 35).
- Temuan untuk QA:
  - TC-AUTH-SES-204 precondition a menyebut user milik Client Alpha, sedangkan dependensi TC-AUTH-SES-96 memakai Client Q2 dengan kuota 2 (seat penuh oleh dua seed); spec memakai Client Q2 (pola yang sama dengan `TC-AUTH-SES-E2E-058`). Expected butir a "tidak pernah muncul di GS Session" tidak menyebut Note yang dicek selain `Concurrent limit reached`; spec mengasersi absennya entri dengan Note itu.
  - TC-AUTH-SES-102 Expected butir b ("tidak ada log baru") dan TC-AUTH-SES-104 Expected butir c ("Tidak ada entri `Session started` kedua") tidak menyebut surface; spec memeriksa GS Session, Session Fixed Asset, dan User Log untuk TC-AUTH-SES-102 (log baru jenis apa pun) serta Session Fixed Asset dan User Log untuk TC-AUTH-SES-104 (lokasi `Session started` menurut TC-AUTH-SES-95 dan 198).
  - TC-AUTH-SES-263 Expected butir c ("tidak mencatat `Session ended` kedua") tidak menyebut surface; spec memakai User Log (tampil `Session ended (Fixed Asset)` menurut TC-AUTH-SES-132). TC itu juga tidak menjelaskan apakah header Fixed Asset (App Switcher) masih tersedia setelah End Product berhasil pada klik kedua; spec mengikuti TC (pola yang sama dengan `TC-AUTH-SES-E2E-033`).
  - TC-AUTH-SES-101, 102, 104, dan 263 tidak mendefinisikan "baru" atau "kedua" terhadap entri yang sudah ada; spec memakai batas waktu langkah pembuka (lihat Notes penentuan entri baru).
  - TC-AUTH-SES-104 dan 263 berlabel `Manual Only`; spec tetap memuatnya dan kebutuhan teknisnya tertulis di Prerequisites.
  - Kemampuan akun Total Control (Global Settings) membaca `Activity Log > Session` milik Fixed Asset tidak dinyatakan di TC (PRD §8 surface #2).
- Pengecualian `P-5` (a): TC-AUTH-SES-104 (konteks web dan mobile) dan TC-AUTH-SES-263 (failure injection) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC memakai user dan baseline sendiri.
