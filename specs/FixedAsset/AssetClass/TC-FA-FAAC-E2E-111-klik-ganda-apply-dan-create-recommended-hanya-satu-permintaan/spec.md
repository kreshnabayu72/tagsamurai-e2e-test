---
id: TC-FA-FAAC-E2E-111-klik-ganda-apply-dan-create-recommended-hanya-satu-permintaan
title: "Klik Ganda Apply dan Create (Recommended) Hanya Memproses Satu Permintaan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-607
coverage:
  web: automated
---

# Klik Ganda Apply dan Create (Recommended) Hanya Memproses Satu Permintaan

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Akun aktor kedua (ganti akun eksplisit di langkah 15): Total Control pada client dengan tabel Asset Class kosong ("tabel kosong lain" pada TC-607). Akun dan kredensialnya tidak tertulis di Pre-setup TC dan disediakan tim FE (lihat Temuan untuk QA); hook `after` mengembalikan sesi ke akun default suite.
- Data seed (kode literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-ASSETS5` dipakai aset (seed Pre-setup); client kedua tanpa Asset Class sehingga EmptyState tabel menampilkan link `Use recommended classes` dan delapan Asset Class rekomendasi tersedia.
- Kemampuan teknis: `Spectra.intercept` parsial di atas backend nyata untuk menahan respons permintaan `Apply` dan `Create` sementara agar state tombol (non-interaktif dengan spinner) dapat diamati, lalu melepasnya segera sesudah diasersi (S-09). Menahan respons hanya untuk mengamati state UI dan bukan kelas fault injection.
- Changelog dibaca lewat kemampuan baca Changelog yang disediakan tim FE/BE: jumlah entri dicatat sebelum aksi dan asersi memakai selisih (audit trail permanen, S-12).
- Jam server dan jam browser sinkron dan tidak digeser spec ini; Effective From dipertahankan pada bulan berjalan (zona waktu General Settings, NC-11).
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: Useful Life `B-ASSETS5` kembali ke nilai seed dan Asset Class hasil Recommended pada client kedua dihapus sehingga tabel kembali kosong.
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-607: Klik ganda Save, Apply, dan Create (Recommended) hanya memproses satu permintaan (bagian Apply)

1. Ketik Search `B-ASSETS5`, tekan Enter
2. Klik link Class Code `B-ASSETS5` di tabel
3. Klik tab `Depreciation`
4. Ubah Useful Life menjadi 48
5. Klik `Save`
6. Catat jumlah entri Changelog sebagai baseline N
7. Tahan respons permintaan `Apply`
8. Pertahankan Effective From bulan berjalan dan klik ganda cepat `Apply`
9. Verifikasi tombol `Apply` non-interaktif dengan spinner
10. Lepaskan tahanan respons
11. Verifikasi dialog `Apply Changes` tertutup (permintaan selesai)
12. Buka Changelog
13. Verifikasi jumlah entri Changelog bertambah tepat 1 dari N, yaitu satu entri Edit Field `Useful Life`
14. Tutup modal Changelog

### TC-FA-FAAC-607: bagian Create (Recommended) pada tabel kosong

15. Ganti akun: logout, lalu login sebagai Total Control pada client dengan tabel Asset Class kosong
16. Buka Fixed Asset > Settings > Accounting > tab Asset Class
17. Klik link `Use recommended classes` pada EmptyState tabel
18. Catat jumlah entri Changelog sebagai baseline N2
19. Tahan respons permintaan `Create`
20. Klik ganda cepat `Create`
21. Verifikasi tombol `Create` non-interaktif dengan spinner
22. Lepaskan tahanan respons
23. Verifikasi delapan Asset Class rekomendasi tampil di tabel, masing-masing tepat satu kali (tidak ada duplikat)
24. Buka Changelog
25. Verifikasi jumlah entri Changelog bertambah tepat 8 dari N2, satu entri Create per Asset Class rekomendasi
26. Tutup modal Changelog

## Notes

1. Urutan dalam spec: bagian Apply pada client pertama lebih dulu, lalu bagian Create (Recommended) pada client kedua dengan tabel kosong; TC-607 satu TC dengan dua aksi pada dua client sehingga akun diganti secara eksplisit di langkah 15 dan sesi dikembalikan ke akun default oleh hook `after`.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (Search untuk menemukan baris target, R-16), langkah 6 dan 18 (baseline Changelog, S-12), langkah 7 dan 19 (menahan respons), langkah 10 dan 22 (melepas tahanan respons), langkah 14 dan 26 (menutup modal Changelog), serta langkah 16 (membuka layar awal setelah ganti akun, S-07). Langkah 12 dan 24 membuka Changelog sebagai langkah observasi karena TC-607 tidak menuliskannya padahal Expected memuat entri log.
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Temuan untuk QA: (a) judul TC-607 menyebut klik ganda Save, Apply, dan Create, tetapi langkah TC hanya mengklik ganda `Apply` dan `Create`; spec mengikuti langkah TC. (b) TC-607 tidak menyebut nilai Useful Life baru (spec memakai 48), akun client dengan "tabel kosong lain", label persis tombol Recommended (spec memakai link `Use recommended classes` seperti TC lain), dan jumlah entri Changelog untuk Create ganda; angka 8 mengikuti delapan Asset Class rekomendasi PRD dengan satu entri Create per Asset Class dan perlu dikonfirmasi QA. (c) Expected TC-607 "satu perubahan dan satu entri log per kejadian" ditulis sebagai selisih Changelog.
