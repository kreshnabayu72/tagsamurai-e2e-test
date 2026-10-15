---
id: TC-AUTH-LP-E2E-043-absence-state-based
title: "Tidak Ada Pencatatan Log pada Kondisi Lock, MFA Tertunda, Agreement Ditinggalkan, dan Policy Tak Ter-resolve"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-120
  - TC-AUTH-LP-124
  - TC-AUTH-LP-90
  - TC-AUTH-LP-157
coverage:
  web: automated
---

# Tidak Ada Pencatatan Log pada Kondisi Lock, MFA Tertunda, Agreement Ditinggalkan, dan Policy Tak Ter-resolve

## Prerequisites

- Mode: FE+BE.
- Seeding: user Activated dan Active dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`), lalu dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Aktor observer log: akun aktor Total Control (Global Settings) di atas login di browser kedua pada hook `before`; browser kedua ditutup di hook `after`.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_WRONG`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua sesi browser bersamaan; reCAPTCHA mode uji di environment; fixture BE pembentukan baris log awal (anchor) untuk user Taufan, Jono, dan Siti di hook `before` (satu entri log awal per user), device terpercaya tanpa gate Agreement dan MFA untuk user Jono, serta riwayat login dan logout kurang dari 30 hari lalu (bukan login pertama, tidak idle) untuk user Taufan; state lock 15 menit pada user beserta baris log "Locked 15 minutes" yang sudah ada; device belum terpercaya (memicu MFA tanpa Agreement); versi Privacy Policy aktif lebih baru dari versi yang disetujui user; menutup tab dan membuka tab baru; state global "versi Privacy Policy aktif tidak ter-resolve atau belum ada versi terpublikasi" (fixture BE) yang dipulihkan pada langkah 49 (tepat sesudah langkah 48 yang menunggu respons login selesai, sebelum pengecekan log) dan di hook `after` sebagai cadangan walau spec gagal di tengah. Spec ini ditaruh serial karena TC-AUTH-LP-157 mengubah state global tersebut dan dijalankan terakhir.
- Kemampuan menuntaskan MFA untuk user Taufan Aditya pada TC-AUTH-LP-124 (langkah 21): TC tidak merinci langkah MFA (pemicu MFA dimiliki modul MFA); kemampuan itu disediakan tim FE/BE tanpa mengarang endpoint atau faktor MFA. Sesi user diakhiri dengan logout pada langkah 24 dan di hook `after`.
- Pencarian baris log memakai nama tampilan dari TC ("Nur A", "Taufan A", "Jono I", "Siti R"; kolom User menampilkan nama singkat, bukan email) dan dibedakan antar run lewat baris anchor dari hook `before` serta penanda waktu sesudah langkah pembuka tiap TC (S-12). Suite berjalan serial (`parallel: false`), sehingga tidak ada spec lain yang menulis baris untuk nama yang sama selama spec ini berjalan.
- TC-AUTH-LP-120: User `Nur Aini` (`nuraini+{runId}-043@qwertysystem.net`) berstatus Activated dan Active, sedang terkunci 15 menit di web dengan baris log "Locked 15 minutes" sudah ada (anchor)
- TC-AUTH-LP-120 data: Email `nuraini+{runId}-043@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD_WRONG`
- TC-AUTH-LP-124: User `Taufan Aditya` (`taufanaditya+{runId}-043@qwertysystem.net`) berstatus Activated dan Active; sudah pernah login dan logout kurang dari 30 hari lalu; versi Privacy Policy terakhir yang disetujui sama dengan versi aktif; browser belum dikenal sebagai device terpercaya (memicu MFA tanpa Agreement); sudah ada baris log sebelumnya (anchor)
- TC-AUTH-LP-124 data: Email `taufanaditya+{runId}-043@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-90: User `Jono Iskandar` (`jonoiskandar+{runId}-043@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui; device terpercaya; tidak memicu MFA; sudah ada baris log sebelumnya (anchor)
- TC-AUTH-LP-90 data: Email `jonoiskandar+{runId}-043@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-157: Tanpa login (guest); user `Siti Rahmawati` (`sitirahmawati+{runId}-043@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif tidak ter-resolve atau belum ada versi terpublikasi (fixture BE); sudah ada baris log sebelumnya (anchor)
- TC-AUTH-LP-157 data: Email `sitirahmawati+{runId}-043@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-120: Percobaan saat lock aktif tidak dicatat

1. Buka halaman Login with Password di browser pertama
2. Ketik "nuraini+{runId}-043@qwertysystem.net" di field Email
3. Ketik nilai `Spectra.env.LP_PASSWORD_WRONG` di field Password
4. Selesaikan reCAPTCHA
5. Klik [Log in]
6. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil ({time} = jam berakhirnya lock)
7. Pindah ke browser kedua (sesi aktor Total Control Global Settings), buka `Global Settings > Activity Log > Session`, lalu cari baris untuk user "Nur A" yang dibuat sesudah langkah 1 dimulai
8. Verifikasi tidak ada baris baru untuk user "Nur A" di `Global Settings > Activity Log > Session` (anchor: baris login sebelumnya tetap tampil)
9. Buka `Global Settings > User > Detail > User Log` untuk user "Nur A", buka tab User Log, dan cari baris yang dibuat sesudah langkah 1 dimulai
10. Verifikasi tidak ada baris baru di `Global Settings > User > Detail > User Log` (anchor: baris sebelumnya tetap tampil)

### TC-AUTH-LP-124: Login yang dialihkan ke MFA belum dicatat Success pada langkah password

11. Pindah ke browser pertama dan buka halaman Login with Password
12. Ketik "taufanaditya+{runId}-043@qwertysystem.net" di field Email
13. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
14. Selesaikan reCAPTCHA
15. Klik [Log in] sampai halaman MFA tampil
16. Verifikasi halaman MFA tampil
17. Pindah ke browser kedua, muat ulang `Global Settings > Activity Log > Session`, lalu cari baris untuk user "Taufan A" yang dibuat sesudah langkah 11 dimulai
18. Verifikasi tidak ada baris baru untuk user "Taufan A" di `Global Settings > Activity Log > Session` (anchor: baris login sebelumnya tetap tampil)
19. Buka `Global Settings > User > Detail > User Log` untuk user "Taufan A", buka tab User Log, dan cari baris yang dibuat sesudah langkah 11 dimulai
20. Verifikasi tidak ada baris baru di `Global Settings > User > Detail > User Log` (anchor: baris sebelumnya tetap tampil)
21. Pindah ke browser pertama dan tuntaskan MFA pada halaman MFA (memakai kemampuan penyelesaian MFA yang disediakan tim FE/BE; TC tidak merinci langkah MFA)
22. Pindah ke browser kedua, muat ulang `Global Settings > Activity Log > Session`, lalu cari baris terbaru untuk user "Taufan A"
23. Verifikasi baris dengan Note "Login with password" baru muncul untuk user "Taufan A" di `Global Settings > Activity Log > Session` setelah user menuntaskan MFA
24. Pindah ke browser pertama dan logout dari Portal — Product Hub

### TC-AUTH-LP-90: Meninggalkan layar Confirm to Continue tanpa Continue tidak dicatat

25. Pindah ke browser pertama dan buka halaman Login with Password
26. Ketik "jonoiskandar+{runId}-043@qwertysystem.net" di field Email
27. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
28. Selesaikan reCAPTCHA
29. Klik [Log in] sampai layar Confirm to Continue tampil
30. Tutup tab tanpa mencentang checkbox atau mengklik [Continue ➔]
31. Buka halaman Login with Password di tab baru
32. Verifikasi halaman Login with Password tampil tanpa sesi aktif
33. Ketik "jonoiskandar+{runId}-043@qwertysystem.net" di field Email
34. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
35. Selesaikan reCAPTCHA
36. Klik [Log in]
37. Verifikasi layar Confirm to Continue tampil lagi
38. Pindah ke browser kedua, muat ulang `Global Settings > Activity Log > Session`, lalu cari baris untuk user "Jono I" yang dibuat sesudah langkah 25 dimulai
39. Verifikasi tidak ada baris baru dengan Note "Consent not given" maupun "Login with password" untuk user "Jono I" di `Global Settings > Activity Log > Session` (anchor: baris sebelumnya tetap tampil)
40. Buka `Global Settings > User > Detail > User Log` untuk user "Jono I", buka tab User Log, dan cari baris yang dibuat sesudah langkah 25 dimulai
41. Verifikasi tidak ada baris baru dengan Note "Consent not given" maupun "Login with password" di `Global Settings > User > Detail > User Log` (anchor: baris sebelumnya tetap tampil)

### TC-AUTH-LP-157: Policy tak ter-resolve, login diblok, tidak ada entri log

42. Aktifkan kondisi versi Privacy Policy aktif tidak ter-resolve atau belum ada versi terpublikasi (fixture BE)
43. Pindah ke browser pertama dan buka halaman Login with Password
44. Ketik "sitirahmawati+{runId}-043@qwertysystem.net" di field Email
45. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
46. Selesaikan reCAPTCHA
47. Klik [Log in]
48. Tunggu respons Login selesai (form Login tetap tampil)
49. Pulihkan kondisi versi Privacy Policy aktif seperti semula (fixture BE)
50. Pindah ke browser kedua, muat ulang `Global Settings > Activity Log > Session`, lalu cari baris untuk user "Siti R" yang dibuat sesudah langkah 43 dimulai
51. Verifikasi tidak ada entri log baru untuk percobaan pada langkah 47 di `Global Settings > Activity Log > Session` (anchor: baris sebelumnya tetap tampil)
52. Buka `Global Settings > User > Detail > User Log` untuk user "Siti R", buka tab User Log, dan cari baris yang dibuat sesudah langkah 43 dimulai
53. Verifikasi tidak ada entri log baru di `Global Settings > User > Detail > User Log` (anchor: baris sebelumnya tetap tampil)

## Notes

- Sumber: `auth/login-password/TestCases/tc-login-password.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: asersi absence (prinsip 13g); semua kasus berbasis state yang disiapkan sebelumnya. TC-AUTH-LP-157 ditaruh terakhir karena mengubah state global versi Privacy Policy (S-10).
- P-2: state "versi Privacy Policy aktif tidak ter-resolve atau belum ada versi terpublikasi" (kegagalan paksa kelas b, fixture BE; langkah 42 dan 49) hanya pemicu untuk mencapai state pada TC-AUTH-LP-157 dan bukan objek asersi spec ini; objek asersi adalah tidak adanya entri log (kelas g, langkah 51 dan 53). Asersi toast, layar, dan perilaku form pada state itu ada di spec `TC-AUTH-LP-E2E-028-resilience-provider-failure-injection`.
- TC-AUTH-LP-157 terbagi lintas spec: asersi toast "Error, failed to log in.", layar Confirm to Continue tidak tampil, form Login tetap terbuka dengan Email dipertahankan, dan Post Condition diuji di spec `TC-AUTH-LP-E2E-028-resilience-provider-failure-injection`; di spec ini hanya asersi tidak adanya entri log (Expected butir d, S-05, prinsip 10).
- TC-AUTH-LP-124 Expected butir c: halaman MFA tampil (langkah 16) dan baris Success baru muncul sesudah MFA dituntaskan (langkah 21 sampai 23). Langkah menuntaskan MFA bukan bagian langkah TC; ia memakai kemampuan yang dinyatakan di Prerequisites dan dicatat di "Temuan untuk QA". Logout pada langkah 24 adalah langkah penghubung (S-03; S-09) agar TC-AUTH-LP-90 mulai dari browser pertama sebagai guest.
- Langkah penghubung (S-03): perpindahan antar browser, pemuatan ulang daftar log, penutupan tab pada langkah 30, dan pengaktifan serta pemulihan state versi Privacy Policy (langkah 42 dan 49, dijamin juga oleh hook `after`) hanya menyiapkan konteks; langkah 48 menunggu respons Login selesai sebelum state dipulihkan agar percobaan pada langkah 47 tidak lolos ke state yang sudah dipulihkan.
- Temuan untuk QA:
  - TC-AUTH-LP-124 tidak memuat langkah MFA padahal Expected butir c menyebut baris "Login with password" muncul setelah MFA dituntaskan, dan tidak menyebut surface mana yang diamati (spec memakai `Global Settings > Activity Log > Session`); mekanisme menuntaskan MFA hanya disebut sebagai kemampuan di Prerequisites tanpa mengarang langkah.
  - TC memakai nama tampilan tetap ("Nur A", "Taufan A", "Jono I", "Siti R") untuk mencari baris log; nama itu tidak unik antar run atau antar spec. Spec memakai baseline (S-12) dan suite serial.
  - TC-AUTH-LP-120 menyatakan baris log "Locked 15 minutes" sudah ada sebagai precondition tanpa menyebut cara terbentuknya; spec menyiapkannya sebagai fixture BE.
  - TC-AUTH-LP-157 tidak memuat langkah atau asersi untuk Post Condition "counter percobaan gagal di-reset (password sudah benar)", dan precondition tidak menyebut kebutuhan reCAPTCHA sedangkan langkah TC 2 menyuruh menyelesaikannya.
  - TC-AUTH-LP-90 memeriksa dua Note berbeda ("Consent not given" dan "Login with password") dalam satu butir; keduanya diverifikasi di kedua surface.
