---
id: TC-FA-FAAC-E2E-107-last-posted-dan-last-exported-period
title: "Last Posted Period dan Last Exported Period: Maju Saat Posting atau Export, Tidak Mundur"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-340
  - TC-FA-FAAC-341
  - TC-FA-FAAC-342
sourceRules: ["F-FAAC-12.k2", "§4.1.2#r4", "F-FAAC-12.k1", "L-10", "J-01", "§4.1.2#r5", "L-11", "J-02"]
smoke: []
dependsOn: []
trace:
  "F-FAAC-12.k2": [6, 8]
  "§4.1.2#r4": 10
  "F-FAAC-12.k1": [14, 23]
  "L-10": [16, 17]
  "J-01": 17
  "§4.1.2#r5": 19
  "L-11": [25, 26]
  "J-02": 26
coverage:
  web: automated
---

# Last Posted Period dan Last Exported Period: Maju Saat Posting atau Export, Tidak Mundur

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-LOCK` dengan Last Posted Period Mar 2026 dan belum punya Last Exported Period (seed Pre-setup sesuai NC-16).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): seed yang menyimulasikan posting periode (Mar 2026, Jan 2026, Apr 2026) dan export periode Mar 2026 untuk `B-LOCK`, karena posting dan export diuji di modul pemiliknya (Depreciation Run, FADR-LOGIC-11i; Export Journal); aktor Asset Class tidak memicunya lewat UI.
- Changelog dibaca lewat kemampuan baca Changelog yang disediakan tim FE/BE: jumlah entri dicatat sebelum aksi dan asersi memakai selisih (audit trail permanen, S-12).
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: Last Posted Period `B-LOCK` kembali Mar 2026 dan Last Exported Period dikosongkan. Efeknya (Last Updated dan entri Changelog) tersisa di audit trail permanen.
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode dan periode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Ketik Search `B-LOCK`, tekan Enter
2. Klik link Class Code `B-LOCK` di tabel

### TC-FA-FAAC-341: Posting periode yang sama atau lebih lama tidak mengubah Last Posted Period

3. Catat jumlah entri Changelog sebagai baseline N
4. Picu seed yang menyimulasikan posting periode `Mar 2026` lalu `Jan 2026` untuk `B-LOCK`
5. Muat ulang Detail `B-LOCK`
6. Verifikasi Last Posted Period tetap `Mar 2026` (tidak mundur dan tidak kosong)
7. Buka Changelog
8. Verifikasi tidak ada entri L-10 baru (jumlah entri Changelog tetap N)
9. Tutup modal Changelog

### TC-FA-FAAC-340: Last Posted Period maju saat periode lebih baru diposting

10. Verifikasi Last Posted Period `Mar 2026`
11. Catat jumlah entri Changelog sebagai baseline N
12. Picu seed yang menyimulasikan posting periode `Apr 2026` untuk `B-LOCK`
13. Muat ulang Detail `B-LOCK`
14. Verifikasi Last Posted Period berubah dari `Mar 2026` menjadi `Apr 2026`
15. Buka Changelog
16. Verifikasi jumlah entri Changelog bertambah 1 dari N
17. Verifikasi entri teratas adalah Edit Field `Last Posted Period` Old `Mar 2026` New `Apr 2026` Modified By `System`
18. Tutup modal Changelog

### TC-FA-FAAC-342: Last Exported Period terisi saat Export Journal berhasil

19. Verifikasi Last Exported Period `—`
20. Catat jumlah entri Changelog sebagai baseline N
21. Picu seed yang menyimulasikan export periode `Mar 2026` untuk `B-LOCK`
22. Muat ulang Detail `B-LOCK`
23. Verifikasi Last Exported Period berubah dari `—` menjadi `Mar 2026`
24. Buka Changelog
25. Verifikasi jumlah entri Changelog bertambah 1 dari N
26. Verifikasi entri teratas adalah Edit Field `Last Exported Period` Old `—` New `Mar 2026` Modified By `System`
27. Tutup modal Changelog
28. Klik breadcrumb `Asset Class`
29. Klik `(←)` pada kotak Search

## Notes

1. Urutan dalam spec: TC-341 (posting yang tidak mengubah apa pun) lebih dulu supaya Last Posted Period masih `Mar 2026`, lalu TC-340 yang memajukannya, dan TC-342 untuk Last Exported Period; seluruhnya pada Detail `B-LOCK` yang dibuka sekali di langkah 2.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (Search untuk menemukan baris target, R-16), langkah 3, 11, dan 20 (baseline Changelog, S-12), langkah 9, 18, dan 27 (menutup modal Changelog), langkah 28 (kembali ke tabel), dan langkah 29 (mengosongkan Search). Langkah 7, 15, dan 24 membuka Changelog sebagai langkah observasi; langkah 10 dan 19 menjadi keadaan awal TC-340 dan TC-342 ("dari ... menjadi ...").
3. Entri Changelog baru dibaca pada baris teratas urutan default `Date` terbaru setelah selisih jumlah dari baseline dibuktikan (S-14).
4. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal dengan periode tertentu; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
5. Temuan untuk QA: TC-341 Expected b ("Tidak ada entri L-10 baru") diasersi sebagai selisih jumlah entri Changelog nol karena kode entri L-10 tidak tampil di UI; anchor positifnya adalah Last Posted Period yang tampil (langkah 6).
