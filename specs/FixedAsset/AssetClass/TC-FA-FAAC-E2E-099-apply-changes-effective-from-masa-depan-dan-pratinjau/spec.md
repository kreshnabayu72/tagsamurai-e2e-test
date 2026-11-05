---
id: TC-FA-FAAC-E2E-099-apply-changes-effective-from-masa-depan-dan-pratinjau
title: "Apply Changes: Pratinjau Assets Affected dan Effective From Masa Depan Menjadwalkan Versi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-309
  - TC-FA-FAAC-312
coverage:
  web: automated
---

# Apply Changes: Pratinjau Assets Affected dan Effective From Masa Depan Menjadwalkan Versi

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-ASSETS` dipakai aset: 1 Asset Name dengan 5 aset aktif, Method Straight Line, Useful Life 60 (Commercial tabel `Straight Line · 5 yrs`), belum pernah diposting, tanpa versi Scheduled.
- Jam: bulan berjalan M mengikuti zona waktu General Settings client (NC-11); jam server dan jam browser sinkron dan tidak digeser spec ini. Effective From yang dipilih TC-309 adalah M+2 (dua bulan sesudah bulan berjalan; contoh TC: Dec 2026 bila bulan berjalan Oct 2026).
- Changelog dibaca lewat kemampuan baca Changelog yang disediakan tim FE/BE: jumlah entri dicatat sebelum aksi dan asersi memakai selisih (audit trail permanen, S-12).
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: versi Scheduled M+2 pada `B-ASSETS` dihapus dan Useful Life berlaku tetap 60.
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode dan nilai itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Ketik Search `B-ASSETS`, tekan Enter
2. Klik link Class Code `B-ASSETS` di tabel
3. Klik tab `Depreciation`
4. Ubah Useful Life dari 60 menjadi 48
5. Klik `Save`

### TC-FA-FAAC-312: Pratinjau Assets affected mengikuti checkbox Apply to existing assets

6. Verifikasi `Assets affected` 5 (jumlah aset aktif) saat `Apply to existing assets` tercentang
7. Hilangkan centang `Apply to existing assets`
8. Verifikasi `Assets affected` 0
9. Centang kembali `Apply to existing assets`
10. Verifikasi `Assets affected` kembali 5
11. Verifikasi pratinjau dihitung ulang setiap checkbox berubah (nilai 5 lalu 0 lalu 5)

### TC-FA-FAAC-309: Apply Changes dengan Effective From di masa depan menjadwalkan versi

12. Catat jumlah entri Changelog sebagai baseline N
13. Pilih Effective From dua bulan sesudah bulan berjalan (M+2)
14. Klik `Apply`
15. Verifikasi halaman tetap di Detail mode Edit
16. Verifikasi toast sukses `Success, asset class has been updated.` tampil di halaman Detail
17. Verifikasi Alert info `Next version starts [MMM YYYY].` dengan bulan M+2 (ditulis MMM YYYY) tampil di atas bar tab
18. Klik breadcrumb `Asset Class` untuk kembali ke tabel
19. Verifikasi nilai berlaku saat ini tidak berubah: Commercial `B-ASSETS` di tabel tetap `Straight Line · 5 yrs` (Useful Life tetap 60)
20. Klik ikon Changelog
21. Verifikasi jumlah entri Changelog bertambah 1 dari N
22. Verifikasi entri teratas adalah Edit Field `Scheduled Version` Old `—` New bulan M+2 (ditulis MMM YYYY)
23. Tutup modal Changelog
24. Klik `(←)` pada kotak Search

## Notes

1. Satu sesi edit Detail `B-ASSETS` dipakai bersama untuk TC-312 dan TC-309: langkah TC nomor 1 sampai 4 (buka Detail, tab Depreciation, ubah Useful Life, Save) identik pada keduanya dan dijalankan sekali di langkah 2 sampai 5. Urutan: pratinjau (TC-312) lebih dulu, lalu Apply yang menyimpan versi Scheduled di akhir.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (Search untuk menemukan baris target, R-16), langkah 12 (baseline Changelog, S-12), langkah 18 (kembali ke tabel), langkah 23 (menutup modal Changelog), dan langkah 24 (mengosongkan Search). Langkah 20 membuka Changelog sebagai langkah observasi (TC-309 mengamati ikon Changelog pada langkah TC nomor 9).
3. Entri Changelog baru dibaca pada baris teratas urutan default `Date` terbaru setelah selisih jumlah dari baseline dibuktikan (S-14).
4. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal dengan 5 aset aktif; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
5. Temuan untuk QA: Expected TC-309 a menyebut "Dec 2026 bila bulan berjalan Oct 2026" sebagai contoh bulan; spec memakai M+2 relatif terhadap bulan berjalan. Nilai Old `—` pada entri Changelog Scheduled Version mengikuti Expected TC.
