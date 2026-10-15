---
id: TC-AUTH-RST-E2E-023-email-change-invalidates-token
title: "Perubahan Email User Meng-invalidate Token Reset Aktif"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-114
  - TC-AUTH-RST-133
  - TC-AUTH-RST-141
coverage:
  web: automated
---

# Perubahan Email User Meng-invalidate Token Reset Aktif

## Prerequisites

- Mode: FE+BE.
- Seeding: tiga user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD` dan tanpa gate Agreement dan MFA (fixture BE); satu token reset aktif per user diterbitkan di hook `before` lewat API Request, tautan dari mail-catcher. Hook `after` menghapus ketiga user lewat id yang dicatat saat seeding; email pengganti `budi.santoso+{runId}-023a@qwertysystem.net` (user a) dan `citra.dewi+{runId}-023b@qwertysystem.net` (user b) menjadi kunci cadangan bagi user yang emailnya berubah lewat UI, dan user c memakai aturan pada TC-AUTH-RST-141; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`.
- Kemampuan teknis: mail-catcher (membaca email konfirmasi perubahan email dan tautannya); reCAPTCHA mode uji; jendela privat ketiga tanpa sesi login untuk pemilik email baru yang membuka tautan konfirmasi perubahan email (terpisah dari jendela guest yang memegang Setup New Password terbuka dan dari jendela admin); jendela guest dan jendela admin terpisah (admin mengubah email user di Global Settings > User > Edit dan membaca Activity Log Session dan User Log; user diidentifikasi lewat email bersuffix); fixture BE yang mengganti email user tanpa invalidasi token oleh callback (hanya TC-AUTH-RST-141).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-114, TC-AUTH-RST-133, TC-AUTH-RST-141: User belum login (guest); browser web.
- TC-AUTH-RST-114: User `Budi Santoso` (`budisantoso+{runId}-023a@qwertysystem.net`) dengan token aktif (tautan di email lama); email baru `budi.santoso+{runId}-023a@qwertysystem.net`.
- TC-AUTH-RST-133: User `Citra Dewi` (`citradewi+{runId}-023b@qwertysystem.net`) dengan token aktif; email baru `citra.dewi+{runId}-023b@qwertysystem.net`; Password dan Confirm Password: `Spectra.env.RST_PASSWORD_NEW`.
- TC-AUTH-RST-141: User `Agus Prasetyo` (email lama `agusprasetyo+{runId}-023c@qwertysystem.net`) Active dengan token aktif untuk email lama; email user kemudian diganti oleh fixture BE menjadi email pengganti `agusprasetyo.baru+{runId}-023c@qwertysystem.net` tanpa invalidasi token oleh callback. Hook `after` menghapus user ini lewat id atau email pengganti itu (email lama sebagai cadangan bila penggantian gagal).

## Test Steps

### Persiapan konteks

1. Buka jendela privat guest (tanpa sesi login), jendela privat admin, dan jendela privat ketiga untuk pemilik email baru (tanpa sesi login); di jendela admin login sebagai akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD` (selesaikan reCAPTCHA), lalu buka Global Settings > Activity Log > Session dengan Filter Activity = "Reset Password"

### TC-AUTH-RST-114: Email change dikonfirmasi meng-invalidate token reset aktif milik email lama

2. Pindah ke jendela admin, buka Global Settings > User > Edit untuk user `budisantoso+{runId}-023a@qwertysystem.net` (cari lewat email) lalu ubah email menjadi `budi.santoso+{runId}-023a@qwertysystem.net`
3. Buka tautan konfirmasi perubahan email dari mail-catcher di tab baru pada jendela privat ketiga (pemilik email baru, tanpa sesi login)
4. Pindah ke jendela guest lalu buka tautan reset dari email lama `budisantoso+{runId}-023a@qwertysystem.net`
5. Verifikasi Halaman 404 tampil dengan Title "Reset Link Expired"
6. Verifikasi Halaman 404 tampil dengan Message "This password reset link has expired. Reset links are valid for 24 hours."
7. Verifikasi Setup New Password tidak dirender

### TC-AUTH-RST-133: Email change dikonfirmasi saat Setup New Password terbuka: submit ditolak

8. Pindah ke jendela guest lalu buka tautan reset milik `citradewi+{runId}-023b@qwertysystem.net` dari mail-catcher sehingga Setup New Password tampil
9. Pindah ke jendela admin, ubah email user `citradewi+{runId}-023b@qwertysystem.net` (cari lewat email) menjadi `citra.dewi+{runId}-023b@qwertysystem.net`
10. Pindah ke jendela privat ketiga (pemilik email baru, tanpa sesi login) lalu buka tautan konfirmasi email baru dari mail-catcher di tab baru
11. Pindah ke jendela admin, buka Activity Log Session lalu terapkan ulang Filter Activity = "Reset Password", lalu catat jumlah entri sebagai baseline B1
12. Pindah ke jendela guest, ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan field Confirm Password lalu klik Button [Reset Password]
13. Verifikasi Halaman 404 tampil dengan Title "Reset Link Expired"
14. Verifikasi Halaman 404 tampil dengan Message "This password reset link has expired. Reset links are valid for 24 hours."
15. Pindah ke jendela admin dan muat ulang Activity Log Session lalu terapkan ulang Filter Activity = "Reset Password"
16. Verifikasi jumlah entri bertambah satu dibanding baseline B1
17. Verifikasi entri baru dengan Note `Reset link expired` untuk user dengan email `citra.dewi+{runId}-023b@qwertysystem.net`: Status Failed (dicari berdasarkan Note dan email, bukan posisi teratas)
18. Pindah ke jendela guest, buka halaman Login with Password lalu login dengan Email `citra.dewi+{runId}-023b@qwertysystem.net` dan Password `Spectra.env.RST_PASSWORD_NEW` (selesaikan reCAPTCHA)
19. Verifikasi login ditolak dengan Alert Danger "Incorrect email or password" (password user tidak berubah menjadi `Spectra.env.RST_PASSWORD_NEW`)

### TC-AUTH-RST-141: Token milik email lama yang belum ter-invalidate callback ditolak 404 dan dicatat

20. Pindah ke jendela admin, muat ulang Activity Log Session lalu terapkan ulang Filter Activity = "Reset Password", lalu catat jumlah entri sebagai baseline B2
21. Pindah ke jendela guest lalu buka tautan reset dari email lama `agusprasetyo+{runId}-023c@qwertysystem.net`
22. Verifikasi Halaman 404 varian Expired tampil
23. Verifikasi Setup New Password tidak dirender
24. Pindah ke jendela admin, muat ulang Activity Log Session lalu terapkan ulang Filter Activity = "Reset Password", lalu periksa entri terbaru milik user dengan email lama `agusprasetyo+{runId}-023c@qwertysystem.net` (email penggantinya `agusprasetyo.baru+{runId}-023c@qwertysystem.net`)
25. Verifikasi jumlah entri bertambah tepat satu dibanding baseline B2
26. Verifikasi entri baru dengan Note "Reset link expired" untuk user dengan email lama `agusprasetyo+{runId}-023c@qwertysystem.net` (email penggantinya `agusprasetyo.baru+{runId}-023c@qwertysystem.net`): Activity "Reset Password", Status "Failed" (dicari berdasarkan Note dan email, bukan posisi teratas)

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Langkah penghubung (S-03): langkah "pindah ke jendela ...", Persiapan konteks (langkah 1), dan membuka halaman Login with Password adalah penghubung antar-konteks. Pada TC-AUTH-RST-133 login dengan email baru dipakai sebagai cara memverifikasi password user tidak berubah (TC memverifikasi bahwa password user tidak berubah menjadi password baru `Spectra.env.RST_PASSWORD_NEW` tanpa menyebut caranya). Login dijalankan sesudah verifikasi log (langkah 18 dan 19) supaya entri login gagal tidak tercampur dalam hitungan Activity Log Session; filter diterapkan ulang pada setiap muat ulang Activity Log Session (langkah 11, 15, 20, dan 24).
- Asersi log memakai selisih jumlah entri terhadap baseline (B1, B2) dan pencarian entri berdasarkan Note dan email, bukan posisi teratas, karena spec lain dalam suite yang menggeser atau membekukan jam server meninggalkan entri bercap waktu di masa depan yang berada di atas entri baru di Activity Log Session (S-12). Tautan konfirmasi email baru dibuka di jendela privat ketiga supaya Setup New Password di jendela guest pada TC-AUTH-RST-133 tetap terbuka dan halaman Activity Log Session di jendela admin tidak berpindah; karena itu halaman Activity Log Session dibuka (bukan dimuat ulang) pada langkah 11.
- Asersi absence Post Condition TC-AUTH-RST-114 butir b ("Tidak ada entri log di modul ini untuk invalidasi tersebut") ada di spec `TC-AUTH-RST-E2E-043-absence-not-logged` (S-05), kelompok perubahan email dikonfirmasi (TC-AUTH-RST-137 Precondition b); spec ini tidak mengasersi absence log.
- Temuan untuk QA: TC-AUTH-RST-141 tidak menyebut cara fixture BE mengganti email tanpa invalidasi callback; dicatat sebagai kebutuhan di Prerequisites beserta email pengganti yang dipakai (S-12, S-15).
- Temuan untuk QA: Post Condition TC-AUTH-RST-114 butir a, TC-AUTH-RST-133, dan TC-AUTH-RST-141 ("Token berstatus invalidated") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
