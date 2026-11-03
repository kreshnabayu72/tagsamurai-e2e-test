---
id: TC-FA-CF-E2E-146-grace-period-fa7-search-changelog-download-dan-lisensi-kembali
title: "Grace Period FA-7: Search, Changelog, Download, Ekspor Aset, dan Lisensi Aktif Kembali"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-663
  - TC-FA-CF-664
  - TC-FA-CF-668
  - TC-FA-CF-669
coverage:
  web: automated
---

# Grace Period FA-7: Search, Changelog, Download, Ekspor Aset, dan Lisensi Aktif Kembali

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Grace (Pre-setup #25). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_GRACE_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Grace (Pre-setup #25): FA-7 sempat aktif lalu diturunkan ke None efektif T-0 dengan Grace Period berjalan (T+10 hari); field Accounting `Cost Center` Text General Active Required Yes bernilai `CC-100` pada aset `A1`; `Asset Tag Class` Text General Inactive. Nilai data mengacu `Fixture.faCustomFields.grace` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis: seed Company Grace (aktifkan kembali lisensi FA-7 dan pemulihan Grace Period berjalan; disediakan tim FE/BE); Column Visibility Asset List; pengujian berkas unduhan CSV (disediakan tim FE); penghapusan preferensi Column Visibility Asset List yang disimpan di browser (disediakan tim FE, bagian 4).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: lisensi FA-7 Company Grace diaktifkan kembali pada langkah 23. Hook `after` memulihkan Grace Period berjalan lewat seed reset Company Grace dan menghapus preferensi Column Visibility Asset List yang disimpan spec di browser pada langkah 19 (bukan `[Reset to Default]`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-663: Search, Filter, dan Sort tab Accounting selama Grace Period

1. Klik tab `Accounting`
2. Verifikasi tabel grup Accounting memuat sedikitnya satu baris
3. Ketik Search `cost`, tekan Enter
4. Verifikasi Search `cost` hanya menampilkan `Cost Center`
5. Klik `(←)` pada kotak Search
6. Klik icon Filter, pilih Active `Inactive`, dan klik `[Apply]`
7. Verifikasi Filter Active `Inactive` hanya menampilkan `Asset Tag Class`
8. Bersihkan filter
9. Klik header `Field Name` sekali
10. Verifikasi Sort Field Name menaik: `Asset Tag Class` lalu `Cost Center`
11. Klik header `Field Name` sekali lagi
12. Verifikasi Sort Field Name menurun: `Cost Center` lalu `Asset Tag Class`

### TC-FA-CF-664: Changelog dan Download tab Accounting selama Grace Period

13. Klik icon Changelog
14. Verifikasi Modal Changelog terbuka tanpa error
15. Tutup Modal Changelog
16. Klik icon Download > `Download as CSV`
17. Verifikasi berkas `Custom-Fields` terunduh
18. Verifikasi berkas memuat baris `Cost Center` dan `Asset Tag Class`

### TC-FA-CF-668: ekspor data aset memuat field Accounting selama Grace Period

19. Buka Asset List dan tampilkan kolom `Cost Center` lewat Column Visibility
20. Klik icon Download > `Download as CSV`
21. Verifikasi berkas CSV memuat kolom `Cost Center`
22. Verifikasi berkas CSV memuat nilai tersimpan `CC-100` pada baris aset `A1`

### TC-FA-CF-669: FA-7 aktif kembali pada Grace Period

23. Aktifkan kembali lisensi FA-7 Company Grace lewat Pre-setup
24. Muat ulang Settings > Custom Fields lalu klik tab `Accounting`
25. Verifikasi tombol `[+ Custom Field]` tampil
26. Verifikasi switch Active Enabled
27. Verifikasi `Cost Center` (Active) dan `Asset Tag Class` (Inactive) tetap dengan konfigurasi dan status tersimpan
28. Buka form registrasi aset pada modul Asset Registration
29. Verifikasi `Cost Center` tampil di form registrasi aset
30. Verifikasi `Cost Center` ditandai Required `Yes`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- TC-FA-CF-669 ditaruh paling akhir karena aktivasi lisensi mengakhiri Grace Period; TC-FA-CF-670 (Grace Period berakhir) ada di spec 180 dengan seed Company Grace sendiri.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 (menutup Search), langkah 8 (membersihkan filter), langkah 15 (menutup Modal Changelog), langkah 23 (aktivasi lisensi lewat seed). Search `cost` di langkah 3 dan Filter di langkah 6 adalah pemicu Expected TC-FA-CF-663; langkah 2 adalah pembanding generik untuk asersi "hanya" (bagian 8b butir 2). Sort tidak dikembalikan karena tidak ada langkah berikutnya yang bergantung pada urutan tabel.
- Temuan untuk QA:
  - Pre-setup TC tidak memuat email akun Total Control Company Grace (Pre-setup #25 hanya mendeskripsikan Company); akun disediakan tim FE.
  - Pre-setup #25 tidak menyebut nilai `Asset Tag Class` pada aset; asersi nilai berkas hanya untuk `Cost Center` aset `A1` (`CC-100`).
