---
id: TC-FA-GRP-E2E-129-groups-list-download-lebih-5000-baris-loading-screen-tanpa-job-background
title: "Groups List Download > 5.000 Baris: Loading Screen Sampai Berkas Siap Tanpa Job Background"
priority: Low
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-423
coverage:
  web: automated
---

# Groups List Download > 5.000 Baris: Loading Screen Sampai Berkas Siap Tanpa Job Background

## Prerequisites

- Mode: FE+BE.
- Kelas harness: e (volume data) dan f (binary buffer).
- Login di hook `before` spec ini sebagai Total Control pada client plan Enterprise dengan tampilan Groups List aktif lebih dari 5.000 baris. Email dan password akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE, nama env password baru `Spectra.env.FA_ENTERPRISE_TC_PASSWORD` didaftarkan tim FE. Halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data: tampilan aktif Groups List > 5.000 baris (disediakan tim FE/BE lewat seeding client Enterprise); N = jumlah baris tampilan aktif, dibaca lewat kemampuan baca jumlah (disediakan tim FE/BE) sebelum uji.
- Kemampuan teknis (disediakan tim FE): penangkapan berkas unduhan browser dan pembacaan jumlah baris berkas CSV.
- Cleanup: tidak ada data yang dibuat spec; seeding client Enterprise bukan milik spec ini.

## Test Steps

1. Klik icon Download
2. Klik `Download as CSV`
3. Verifikasi Loading screen tampil
4. Verifikasi tidak ada notifikasi in-app dan tidak ada jendela unduh 24 jam tampil
5. Tunggu sampai berkas selesai diunduh
6. Verifikasi berkas `Groups.csv` terunduh langsung setelah Loading screen hilang
7. Verifikasi Loading screen tidak lagi tampil
8. Verifikasi jumlah baris data berkas `Groups.csv` sama dengan N (lebih dari 5.000 baris)
9. Verifikasi tidak ada notifikasi in-app tampil sesudah berkas terunduh

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah 5 adalah langkah penghubung tanpa `Verifikasi` (menunggu berkas siap; batas tunggu mengikuti idiom polling, bukan jeda waktu tetap).
- Asersi "tidak ada job background" tidak dapat diamati langsung; diamati lewat tidak adanya notifikasi in-app dan jendela unduh 24 jam (Expected b TC-FA-GRP-423).
- Spec kelas e dan f (satu TC); isi berkas tidak diasersi selain jumlah baris.
- Temuan untuk QA:
  - TC-FA-GRP-423 memerlukan client plan Enterprise dengan tampilan > 5.000 baris; akun dan client tersebut tidak tertulis di Pre-setup TC.
  - Password akun aktor memakai env baru `FA_ENTERPRISE_TC_PASSWORD`; perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
