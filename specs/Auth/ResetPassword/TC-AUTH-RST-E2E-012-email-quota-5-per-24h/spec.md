---
id: TC-AUTH-RST-E2E-012-email-quota-5-per-24h
title: "Kuota 5 Percobaan per 24 Jam per Email pada Request"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-30
  - TC-AUTH-RST-31
  - TC-AUTH-RST-148
  - TC-AUTH-RST-34
  - TC-AUTH-RST-32
  - TC-AUTH-RST-117
coverage:
  web: automated
---

# Kuota 5 Percobaan per 24 Jam per Email pada Request

## Prerequisites

- Mode: FE+BE, dengan fixture BE untuk counter percobaan per email.
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), dengan password aktif `Spectra.env.RST_PASSWORD`. Counter percobaan per email dalam 24 jam dan cooldown 60 detik diatur lewat fixture BE per user (kemampuan teknis yang diminta dari tim BE). User dihapus dan counter dipulihkan di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: fixture BE untuk counter per email; mail-catcher dengan pembacaan jumlah email per alamat (baseline sebelum aksi, dibandingkan sesudahnya); reCAPTCHA mode uji; jendela guest dan jendela admin terpisah (admin membaca Activity Log Session dan User Log).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-30, TC-AUTH-RST-31, TC-AUTH-RST-148, TC-AUTH-RST-34, TC-AUTH-RST-32, TC-AUTH-RST-117: User belum login (guest); browser web.
- TC-AUTH-RST-30: User `Dewi Lestari` (`dewilestari+{runId}-012a@qwertysystem.net`) Active; 4 percobaan dalam 24 jam terakhir, cooldown sudah lewat.
- TC-AUTH-RST-31: User `Fajar Nugroho` (`fajarnugroho+{runId}-012b@qwertysystem.net`) Active; 5 percobaan dalam 24 jam terakhir, cooldown sudah lewat.
- TC-AUTH-RST-148: User `Gita Nugroho` (`gitanugroho+{runId}-012c@qwertysystem.net`) Active; 5 percobaan dalam 24 jam terakhir, cooldown sudah lewat; data Email: `GitaNugroho+{runId}-012C@QwertySystem.net`.
- TC-AUTH-RST-34: User `Siti Rahmawati` (`sitirahmawati+{runId}-012d@qwertysystem.net`) Active tanpa percobaan. Pada titik ini `fajarnugroho+{runId}-012b@qwertysystem.net` dan `gitanugroho+{runId}-012c@qwertysystem.net` sudah melewati kuota 5 percobaan (urutan spec: TC-AUTH-RST-31 dan 148 berjalan lebih dulu, masing-masing menghasilkan Request ke-6 yang dicatat Failed).
- TC-AUTH-RST-32: User `Tono Kurniawan` (`tonokurniawan+{runId}-012e@qwertysystem.net`) Inactive; 5 percobaan dalam 24 jam, cooldown sudah lewat.
- TC-AUTH-RST-117: User `Indah Lestari` (`indahlestari+{runId}-012f@qwertysystem.net`) Active; 5 percobaan reset dalam 24 jam, cooldown sudah lewat, dan sudah menyelesaikan Submit New Password sukses (diatur fixture BE).

## Test Steps

### Persiapan konteks

1. Buka jendela privat guest (tanpa sesi login) dan jendela privat admin; di jendela admin login sebagai akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD` (selesaikan reCAPTCHA), lalu buka Global Settings > Activity Log > Session dengan Filter Activity = "Reset Password"

### TC-AUTH-RST-30: Request ke-5 dalam 24 jam masih diproses

2. Pindah ke jendela guest, buka halaman Reset Password (Request), lalu catat jumlah email di mail-catcher untuk `dewilestari+{runId}-012a@qwertysystem.net` sebagai baseline
3. Ketik `dewilestari+{runId}-012a@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password]
4. Verifikasi browser menuju halaman Email Sent!
5. Verifikasi tidak ada toast
6. Verifikasi jumlah email di mail-catcher untuk `dewilestari+{runId}-012a@qwertysystem.net` bertambah 1 dibanding baseline

### TC-AUTH-RST-31: Request ke-6 dalam 24 jam ditampilkan identik dengan sukses tanpa email baru

7. Pindah ke jendela admin, muat ulang Activity Log Session dan buka Global Settings > User > Detail > User Log untuk user dengan email `fajarnugroho+{runId}-012b@qwertysystem.net`, lalu catat jumlah baris dan baris teratas kedua surface sebagai baseline
8. Catat jumlah email di mail-catcher untuk `fajarnugroho+{runId}-012b@qwertysystem.net` sebagai baseline
9. Pindah ke jendela guest, buka halaman Reset Password (Request), ketik `fajarnugroho+{runId}-012b@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password]
10. Verifikasi browser menuju halaman Email Sent!
11. Verifikasi tidak ada toast
12. Verifikasi Message tampil "We've sent a password reset link to fajarnugroho+{runId}-012b@qwertysystem.net. Please check your inbox and follow the instructions." (sama dengan hasil sukses)
13. Verifikasi jumlah email di mail-catcher untuk `fajarnugroho+{runId}-012b@qwertysystem.net` sama dengan baseline
14. Pindah ke jendela admin, muat ulang Activity Log Session dan buka Global Settings > User > Detail > User Log untuk user dengan email `fajarnugroho+{runId}-012b@qwertysystem.net`
15. Verifikasi jumlah baris Activity Log Session dan User Log masing-masing bertambah tepat satu dibanding baseline
16. Verifikasi baris baru teratas pada Activity Log Session: Activity `Reset Password`, Status Failed, Note `Too many reset attempts`
17. Verifikasi baris baru teratas pada User Log: Activity `Reset Password`, Status Failed, Note `Too many reset attempts`

### TC-AUTH-RST-148: Variasi huruf besar tidak menghindari kuota

18. Di jendela admin, buka User Log user dengan email `gitanugroho+{runId}-012c@qwertysystem.net` lalu catat jumlah baris dan baris teratas Activity Log Session dan User Log sebagai baseline
19. Catat jumlah email di mail-catcher untuk `gitanugroho+{runId}-012c@qwertysystem.net` sebagai baseline
20. Pindah ke jendela guest, buka halaman Reset Password (Request), ketik `GitaNugroho+{runId}-012C@QwertySystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password]
21. Verifikasi browser menuju halaman Email Sent!
22. Verifikasi tidak ada toast
23. Verifikasi Message tampil "We've sent a password reset link to GitaNugroho+{runId}-012C@QwertySystem.net. Please check your inbox and follow the instructions." (sama dengan hasil sukses)
24. Verifikasi jumlah email di mail-catcher untuk `gitanugroho+{runId}-012c@qwertysystem.net` sama dengan baseline
25. Pindah ke jendela admin, muat ulang Activity Log Session dan buka User Log user dengan email `gitanugroho+{runId}-012c@qwertysystem.net`
26. Verifikasi jumlah baris Activity Log Session dan User Log masing-masing bertambah tepat satu dibanding baseline
27. Verifikasi baris baru teratas pada Activity Log Session: Activity `Reset Password`, Status Failed, Note `Too many reset attempts`
28. Verifikasi baris baru teratas pada User Log: Activity `Reset Password`, Status Failed, Note `Too many reset attempts`

### TC-AUTH-RST-34: Batas satu akun tidak memblokir akun lain

29. Pindah ke jendela guest, buka halaman Reset Password (Request), lalu catat jumlah email di mail-catcher untuk `sitirahmawati+{runId}-012d@qwertysystem.net` sebagai baseline
30. Ketik `sitirahmawati+{runId}-012d@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password]
31. Verifikasi browser menuju halaman Email Sent!
32. Verifikasi tidak ada toast
33. Verifikasi jumlah email di mail-catcher untuk `sitirahmawati+{runId}-012d@qwertysystem.net` bertambah 1 dibanding baseline

### TC-AUTH-RST-32: Akun Inactive yang melewati batas per email dicatat Too many reset attempts

34. Pindah ke jendela admin, muat ulang Activity Log Session lalu catat jumlah baris dan baris teratas sebagai baseline
35. Pindah ke jendela guest, buka halaman Reset Password (Request), ketik `tonokurniawan+{runId}-012e@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password]
36. Verifikasi browser menuju halaman Email Sent!
37. Verifikasi tidak ada toast
38. Verifikasi caption "Your account is inactive" tidak tampil
39. Pindah ke jendela admin dan muat ulang Activity Log Session
40. Verifikasi jumlah baris Activity Log Session bertambah tepat satu dibanding baseline
41. Verifikasi baris baru teratas: Status Failed, Note `Too many reset attempts` (bukan `Account is inactive`)

### TC-AUTH-RST-117: Counter percobaan reset dipulihkan oleh Submit sukses

42. Pindah ke jendela guest, buka halaman Reset Password (Request), lalu catat jumlah email di mail-catcher untuk `indahlestari+{runId}-012f@qwertysystem.net` sebagai baseline
43. Ketik `indahlestari+{runId}-012f@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password]
44. Verifikasi browser menuju halaman Email Sent!
45. Verifikasi tidak ada toast
46. Verifikasi jumlah email di mail-catcher untuk `indahlestari+{runId}-012f@qwertysystem.net` bertambah 1 dibanding baseline (counter percobaan reset sudah di-reset oleh Submit sukses)

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`. TC-AUTH-RST-34 bergantung pada urutan spec: pada titik itu `fajarnugroho+{runId}-012b@qwertysystem.net` dan `gitanugroho+{runId}-012c@qwertysystem.net` sudah melewati kuota karena TC-AUTH-RST-31 dan TC-AUTH-RST-148 berjalan lebih dulu. Request di TC-AUTH-RST-34 hanya dikirim untuk `sitirahmawati+{runId}-012d@qwertysystem.net` yang tanpa percobaan dan tetap diproses, yaitu membuktikan kuota yang habis pada user lain tidak memblokirnya.
- Urutan: kasus yang masih diproses (TC-AUTH-RST-30, 34, 117) tidak mengubah kuota user lain; user tiap TC terpisah karena TC sumber berbagi `fajarnugroho` dan `dewilestari` yang counter-nya diatur ulang per TC.
- TC-AUTH-RST-117 menyatakan Submit sukses sebelumnya "diatur fixture BE"; alur Submit-nya sendiri diuji di spec `TC-AUTH-RST-E2E-028-submit-success-and-already-used`.
- Counter fixture dan akun dipulihkan di hook `after`.
- Langkah penghubung (S-03): langkah 1 ("Persiapan konteks": jendela guest dan admin, login admin, buka Activity Log Session dengan Filter), perpindahan jendela guest dan admin (langkah 2, 7, 9, 14, 20, 25, 29, 34, 35, 39, 42), muat ulang Activity Log Session dan pembukaan User Log (langkah 7, 14, 18, 25, 34, 39), pencatatan baseline log (langkah 7, 18, 34), serta pencatatan baseline jumlah email di mail-catcher (langkah 2, 8, 19, 29, 42; S-12).
- Jumlah langkah 46 melampaui ±35: alasan Verifikasi dipecah per klausa sesuai S-01 (28 dari 46 langkah adalah Verifikasi; 18 sisanya aksi dan langkah penghubung). Satu topik (kuota 5 per 24 jam per email), satu kelas harness (fixture counter, mail-catcher, jendela admin), tanpa prefix login berulang (login admin sekali di langkah 1).
- Temuan untuk QA: Post Condition TC-AUTH-RST-30 (token baru, counter 5), TC-AUTH-RST-31 dan 148 (tidak ada token baru, counter tetap 5), TC-AUTH-RST-32 (tidak ada token baru dan tidak ada email), TC-AUTH-RST-34 (token aktif baru terbit untuk Siti Rahmawati), dan TC-AUTH-RST-117 (counter menjadi 1) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
