---
id: TC-FA-FAAC-E2E-175-log-pembatalan-versi-scheduled-dan-last-posted-exported
title: "Log Pembatalan Versi Scheduled dan Perubahan Last Posted dan Last Exported Period"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-537
  - TC-FA-FAAC-538
coverage:
  web: automated
---

# Log Pembatalan Versi Scheduled dan Perubahan Last Posted dan Last Exported Period

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Nama tampil akun pada kolom Modified By: `Rina W` (format [First Name] [Last Initial], menurut TC-541 sampai TC-550). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-SCHED3` dengan versi Scheduled M+2; `B-LOCK` dengan Last Posted Period Mar 2026.
- Kemampuan baca log yang disediakan tim FE/BE: jumlah entri Changelog, System Log aktor, dan Activity Log FAMS dibaca tepat sebelum aksi pemicu tiap TC (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Kemampuan teknis: fixture BE untuk memicu seed posting dan export periode (NC-16).
- Jam server dan jam browser sinkron dan tidak digeser spec ini; bulan berjalan M mengikuti zona waktu General Settings client (NC-11). Kolom Date entri log dibandingkan dengan waktu aksi yang dicatat sesudah aksi, toleransi satu menit.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: B-SCHED3 kembali dengan versi Scheduled M+2; B-LOCK kembali ke Last Posted Period Mar 2026 tanpa Last Exported Period.
- Kode dan nama seed memakai nilai literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-537: Log pembatalan versi Scheduled

1. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
2. Klik link Class Code `B-SCHED3` di tabel
3. Klik tombol `Cancel scheduled version` pada Alert
4. Klik `Cancel version` pada dialog `Cancel Scheduled Version`
5. Kembali ke tabel Asset Class lewat Breadcrumb
6. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
7. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
8. Verifikasi baris teratas Changelog: Action `Edit`, Field `Scheduled Version`, Old Value `[MMM YYYY]` (M+2), New Value `—`
9. Tutup modal Changelog
10. Buka Global Settings > User > Detail User milik aktor > Tab System Log
11. Verifikasi jumlah entri System Log bertambah tepat 1 dari Ns
12. Verifikasi baris teratas System Log aktor: entri yang sama dengan Name `B-SCHED3`
13. Buka Activity Log FAMS
14. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari Na
15. Verifikasi baris teratas Activity Log: baris yang sama dengan Object `Asset Class`, Name `B-SCHED3`, dan Modified By `Rina W`

### TC-FA-FAAC-538: Last Posted dan Last Exported Period dicatat oleh System pada Changelog dan Activity Log

16. Buka Fixed Asset > Settings > Accounting > tab Asset Class
17. Catat jumlah entri Changelog (Nc) dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
18. Picu seed posting periode Apr 2026 dan export periode Mar 2026 untuk `B-LOCK` lewat fixture BE
19. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
20. Verifikasi jumlah entri Changelog bertambah tepat 2 dari Nc
21. Verifikasi dua baris teratas Changelog: Field `Last Posted Period` dan Field `Last Exported Period` dengan Modified By `System`
22. Tutup modal Changelog
23. Buka Activity Log FAMS
24. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari Na
25. Verifikasi dua baris teratas Activity Log: Field `Last Posted Period` dan Field `Last Exported Period` dengan Modified By `System`

## Notes

1. Pembagian TC lintas spec (S-05): Expected TC-538 butir b (System Log tidak memuat entri L-10 dan L-11) diasersi di spec 166 dengan aksi nyata dan baseline sendiri; spec ini mengasersi butir a (Changelog dan Activity Log). TC-536 ada di spec 161.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 dan awal tiap blok TC (baseline log) dan langkah kembali ke layar awal.
3. Baseline log (S-12): jumlah entri dicatat ulang sebelum aksi pemicu tiap TC lewat kemampuan baca log. Entri baru dibaca pada baris teratas urutan default Date terbaru sesudah selisih jumlah dari baseline dibuktikan (S-14); bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
4. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dan nama dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
5. Temuan untuk QA: (a) TC-537 menulis "Alert dan D-24" tanpa label tombol; spec memakai `Cancel scheduled version` dan `Cancel version` seperti spec Cancel Scheduled Version lain di suite ini. (b) Expected a TC-538 tidak menyebut Old Value dan New Value baris Last Posted dan Last Exported Period; spec hanya mengasersi Field dan Modified By.
