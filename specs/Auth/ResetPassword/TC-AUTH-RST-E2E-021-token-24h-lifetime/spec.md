---
id: TC-AUTH-RST-E2E-021-token-24h-lifetime
title: "Masa Berlaku Token Reset 24 Jam: 23:59, 24:00, 24:01, dan Form Terbuka"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-RST-56
  - TC-AUTH-RST-149
  - TC-AUTH-RST-55
  - TC-AUTH-RST-131
  - TC-AUTH-RST-134
coverage:
  web: automated
---

# Masa Berlaku Token Reset 24 Jam: 23:59, 24:00, 24:01, dan Form Terbuka

## Prerequisites

- Mode: FE+BE (kelas d: time-travel).
- Seeding: empat user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`. Satu token reset aktif per user diterbitkan di hook `before` lewat API Request secara berurutan (token A, B, C, lalu D), sehingga tiap token punya waktu terbit sendiri (Ta, Tb, Tc, Td); waktu terbit tiap token dibaca di hook `before` lewat kemampuan membaca waktu terbit token, disediakan tim FE/BE; tautan diambil dari mail-catcher. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`.
- Kemampuan teknis: pengatur jam server uji yang dapat diset absolut dan dibekukan (batas eksak TC-AUTH-RST-149 diset ke Tb + 24 jam 0 detik, bukan digeser relatif); mail-catcher; reCAPTCHA mode uji; jendela guest dan jendela admin terpisah (admin membaca Activity Log Session dan User Log, user dicari lewat email bersuffix). Umur token dihitung murni di server dan tidak diamati lewat UI, sehingga hanya jam server yang diatur.
- State global yang diubah: jam server uji (dibekukan pada langkah 3 sampai 14 dan langkah 18 sampai 23). Suite berjalan serial (`parallel: false`). Pemulihan: jam server dikembalikan ke waktu nyata sebagai langkah aksi (langkah 15 dan 24, sebelum admin membuka Activity Log Session atau User Log) dan di hook `after` sebagai cadangan (tetap berjalan walau spec gagal di tengah).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-56, TC-AUTH-RST-149, TC-AUTH-RST-55, TC-AUTH-RST-131, TC-AUTH-RST-134: User belum login (guest); browser web.
- TC-AUTH-RST-56: User `Budi Santoso` (`budisantoso+{runId}-021a@qwertysystem.net`), token A terbit pada Ta.
- TC-AUTH-RST-149: User `Citra Dewi` (`citradewi+{runId}-021b@qwertysystem.net`), token B terbit pada Tb.
- TC-AUTH-RST-55: User `Dewi Lestari` (`dewilestari+{runId}-021c@qwertysystem.net`), token C terbit pada Tc.
- TC-AUTH-RST-131: User `Eko Santoso` (`ekosantoso+{runId}-021d@qwertysystem.net`), token D terbit pada Td; data Password dan Confirm Password: `Spectra.env.RST_PASSWORD_NEW`.
- TC-AUTH-RST-134: entri log dari submit TC-AUTH-RST-131 (user `Eko Santoso`, email `ekosantoso+{runId}-021d@qwertysystem.net`).

## Test Steps

### Persiapan konteks

1. Buka jendela privat guest (tanpa sesi login) dan jendela privat admin; di jendela admin login sebagai akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD` (selesaikan reCAPTCHA)
2. Pindah ke jendela guest lalu buka tautan token D sehingga Setup New Password tampil; biarkan tab ini terbuka

### TC-AUTH-RST-56: Tautan berusia kurang dari 24 jam masih valid

3. Set jam server uji ke Ta + 23 jam 59 menit 0 detik lalu bekukan
4. Buka tautan token A di tab baru
5. Verifikasi Setup New Password tampil dengan Subtitle "Set a new password to log in for budisantoso+{runId}-021a@qwertysystem.net."

### TC-AUTH-RST-149: Tautan berusia tepat 24 jam masih valid

6. Set jam server uji ke tepat Tb + 24 jam 0 menit 0 detik lalu bekukan
7. Buka tautan token B di tab baru
8. Verifikasi Setup New Password tampil dengan Subtitle "Set a new password to log in for citradewi+{runId}-021b@qwertysystem.net."
9. Verifikasi Halaman 404 tidak tampil

### TC-AUTH-RST-55: Tautan berusia lebih dari 24 jam kedaluwarsa

10. Set jam server uji ke Td + 24 jam 1 menit (lebih lambat dari Tc + 24 jam 1 menit, sehingga token C dan token D keduanya berusia lebih dari 24 jam) lalu bekukan
11. Buka tautan token C di tab baru
12. Verifikasi Halaman 404 tampil dengan Title "Reset Link Expired"
13. Verifikasi Halaman 404 tampil dengan Message "This password reset link has expired. Reset links are valid for 24 hours."
14. Verifikasi Setup New Password tidak dirender

### TC-AUTH-RST-131: Submit setelah token melewati 24 jam saat Setup New Password sudah terbuka

15. Kembalikan jam server uji ke waktu nyata
16. Pindah ke jendela admin, buka Global Settings > Activity Log > Session lalu terapkan Filter Activity = "Reset Password" dan catat jumlah entri sebagai baseline B1
17. Buka Global Settings > User > Detail > User Log untuk user `ekosantoso+{runId}-021d@qwertysystem.net` (cari lewat email) dan catat jumlah entri sebagai baseline B2
18. Set jam server uji ke Td + 24 jam 1 menit lalu bekukan (token D berusia lebih dari 24 jam)
19. Pindah ke tab token D di jendela guest (Setup New Password sudah terbuka sejak sebelum jam server digeser)
20. Ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan field Confirm Password
21. Klik Button [Reset Password]
22. Verifikasi Halaman 404 tampil dengan Title "Reset Link Expired"
23. Verifikasi Halaman 404 tampil dengan Message "This password reset link has expired. Reset links are valid for 24 hours."

### TC-AUTH-RST-134: Submit dengan token expired tercatat Failed / Reset link expired

24. Kembalikan jam server uji ke waktu nyata
25. Pindah ke jendela admin dan muat ulang Activity Log Session lalu terapkan ulang Filter Activity = "Reset Password" lalu muat ulang User Log user `ekosantoso+{runId}-021d@qwertysystem.net`
26. Verifikasi Activity Log Session dan User Log masing-masing bertambah satu entri dibanding baseline B1 dan B2
27. Verifikasi entri baru dengan Note `Reset link expired` untuk user dengan email `ekosantoso+{runId}-021d@qwertysystem.net` pada kedua surface: Activity `Reset Password`, Status Failed (dicari berdasarkan Note dan email, bukan posisi teratas)

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Urutan: geser jam hanya maju, sehingga 23:59, lalu 24:00, lalu 24:01 berurutan; token D dibuka sebelum jam digeser supaya form sudah terbuka pada TC-AUTH-RST-131 (urutan TC-AUTH-RST-131 digeser ke sesudah TC-AUTH-RST-55 karena waktunya 24:01).
- Pemulihan jam (S-09): langkah 15 dan 24 mengembalikan jam server ke waktu nyata sebelum admin membuka Activity Log Session dan User Log, sehingga sesi admin dan timestamp log tidak dibaca pada jam beku. Baseline B1 dan B2 (langkah 16 dan 17) diambil sesudah pembukaan tautan token A, B, dan C dan pada jam nyata; jam server lalu diset absolut lagi pada langkah 18 untuk submit TC-AUTH-RST-131.
- Entri log yang dibuat saat jam server diset ke masa depan (pembukaan tautan token C pada langkah 11 dan submit pada langkah 21) bercap waktu sekitar 24 jam di depan jam nyata, sehingga setelah jam dipulihkan entri baru dari spec lain bercap lebih lama dan berada di bawahnya. Karena itu asersi log memakai selisih jumlah entri terhadap baseline B1 dan B2 dan pencarian entri berdasarkan Note dan email, bukan posisi teratas (S-12).
- Batas eksak: jam server diset absolut relatif terhadap waktu terbit tiap token (bukan digeser relatif dan bukan "T0 yang sama", karena token diterbitkan berurutan) dan dibekukan, supaya latensi eksekusi tidak menghasilkan 24:00:xx.
- Langkah penghubung (S-03): Persiapan konteks (langkah 1 dan 2), pindah jendela atau tab, pemulihan jam (langkah 15 dan 24), dan membuka tautan di tab baru bukan asersi TC.
- Temuan untuk QA: titik tepat 24 jam ditulis di TC-AUTH-RST-149 sebagai masih valid (`auth-foundation.md` §2: "lebih dari 24 jam"); titik tepat cooldown 60 detik dan tepi jendela rate limit ditahan `GAP-467`.
- Temuan untuk QA: Post Condition TC-AUTH-RST-56, TC-AUTH-RST-149 ("Token tetap berstatus active"), TC-AUTH-RST-55 ("Token berstatus expired"), dan TC-AUTH-RST-131 ("password user tidak berubah") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
