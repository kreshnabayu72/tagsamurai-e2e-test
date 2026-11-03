---
id: TC-FA-RP-E2E-091-volume-data-company-export-download-changelog-di-atas-5-000
title: "Volume data Company Export: Download Changelog di atas 5.000 baris"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-755
coverage:
  web: automated
---

# Volume data Company Export: Download Changelog di atas 5.000 baris

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control `Company Export` (Pre-setup #29), akun disediakan tim FE (email tidak tertulis di Pre-setup TC, lihat Temuan untuk QA), `Spectra.env.FA_EXPORT_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_EXPORT_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #29 `Company Export`: log 5.001 entri Changelog (seeding lewat API disediakan tim FE/BE). Spec tidak mengubah data.
- Kemampuan teknis (disediakan tim FE/BE): penangkapan berkas unduhan browser dan pembaca jumlah baris berkas CSV; pembacaan jumlah entri Changelog sebelum aksi; pembacaan status job ekspor.

## Test Steps

### TC-FA-RP-755: Download Changelog di atas 5.000 baris memakai loading screen tanpa job background

1. Klik Tab `Total Control`
2. Klik ikon Changelog pada toolbar
3. Catat jumlah entri Changelog `Company Export` yang dibaca lewat kemampuan baca FE/BE sebagai N (N sedikitnya 5.001)
4. Klik ikon Download lalu `Download as CSV`
5. Verifikasi loading screen tampil sampai berkas siap
6. Verifikasi tidak ada notifikasi in-app
7. Verifikasi berkas langsung terunduh
8. Verifikasi berkas memuat seluruh baris Changelog: jumlah baris data sama dengan N dan di atas 5.000
9. Verifikasi tidak ada job background (dibaca lewat kemampuan baca status ekspor FE/BE)
10. Verifikasi tidak ada jendela 24 jam: tidak ada pesan jendela 24 jam di layar

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-755).
- Kelas e (volume data): ambang 5.001 baris pada tenant `Company Export`.
- Langkah penghubung (S-03): membuka Tab Total Control dan modal Changelog; mencatat N sebagai baseline (langkah 3).
- Urutan Verifikasi mengikuti bagian 8b butir 5 dan 11: loading screen (state sementara) diasersi segera setelah pemicu, lalu absence notifikasi in-app sebelum asersi artefak, lalu berkas terunduh sebagai bukti pemicu diproses.
- Temuan untuk QA:
  - Expected b TC-FA-RP-755 menyebut "seluruh 5.001 baris" sebagai angka absolut; audit trail permanen tumbuh sehingga angka absolut tidak sah (S-12). Spec membandingkan jumlah baris berkas dengan N yang dibaca sebelum unduh dan menegaskan N di atas 5.000.
  - TC-FA-RP-755 tidak menyebut apakah baris header berkas dihitung dalam 5.001 baris; spec menghitung baris data saja.
  - Cara mengamati "tidak ada job background" dan "tidak ada jendela 24 jam" tidak disebut TC; spec memakai kemampuan baca status ekspor yang disediakan tim FE/BE dan mengamati pesan di layar tanpa mengarang endpoint (S-13).
  - Akun Total Control `Company Export` tidak tertulis di Pre-setup TC; dicatat "disediakan tim FE" (S-11).
