---
id: TC-FA-TAG-E2E-085-replace-nasib-tag-lama-available-damaged-missing-dan-keluar-bagian-3
title: "Tag QR yang Dilaporkan Tidak Pernah Masuk Tab To Be Returned"
priority: Low
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1379
coverage:
  web: automated
---

# Tag QR yang Dilaporkan Tidak Pernah Masuk Tab To Be Returned

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Staff Auditor (tidak memegang Manage asset & TAG) `staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD`. Login di hook `before` spec ini; halaman dibuka di langkah pertama (hook suite `beforeEach` dikecualikan, lihat `suite.md`). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Akun aktor tambahan (ganti akun lewat langkah eksplisit): Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: task Existence Audit dengan item AST-0044 ('Excavator 20 Ton - 44', Group Plant B) berstatus In Audit; Tag RFID `RF-00132` dan Tag QR `QR-00232` keduanya Paired pada AST-0044 tanpa laporan terbuka. Report Type `Missing` dan Note `QR hilang` adalah nilai yang diketik pada dialog Report TAG.
- Catatan akun: akun pertama (Staff Auditor tanpa Manage asset & TAG) membuka modul Audit, bukan halaman Fixed Asset > TAG; Total Control dipakai lewat ganti akun eksplisit untuk membuka tab To Be Returned.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: laporan Tag pada AST-0044 dibuat oleh aksi Report TAG (langkah 6); tidak ada Replace yang di-submit, sehingga stok Tag per tipe di registri Global tidak berubah dan Tag `QR-00232` tetap Paired (langkah 13); fixture backend memulihkan laporan di hook `before` dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).
- Nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 6).

## Test Steps

### TC-FA-TAG-1379: Tag QR yang dilaporkan tidak pernah masuk To Be Returned

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
2. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 44
3. Centang opsi "QR"
4. Pilih Report Type "Missing"
5. Isi Textarea "Note" dengan "QR hilang"
6. Klik tombol [Submit]
7. Tunggu aksi selesai (dialog Report TAG tertutup dan tombol aktif kembali)
8. Ganti akun: klik Logout
9. Login sebagai Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`)
10. Buka Fixed Asset > TAG > To Be Returned
11. Verifikasi tab To Be Returned aktif dan tabelnya termuat
12. Verifikasi tab To Be Returned tidak memuat `QR-00232`
13. Verifikasi (baca lewat fixture BE) Tag `QR-00232` tetap Paired pada AST-0044

## Notes

- Langkah penghubung (S-03): Langkah tunggu aksi selesai dan ganti akun ke Total Control sebelum membuka tab To Be Returned; `Verifikasi` tab To Be Returned aktif dan termuat ditambahkan sebagai anchor positif asersi absence (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-TAG-336 sampai 339 ada di spec 074.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- A-15: nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 6).
- Temuan untuk QA:
  - Hook suite `beforeEach` membuka Fixed Asset > TAG untuk akun aktor pertama; akun Staff Auditor tanpa Manage asset & TAG tidak berhak atas halaman itu; spec ini dikecualikan di `suite.md` bagian Hook sehingga halaman yang diuji dibuka di langkahnya sendiri.
  - Langkah pembuka TC memakai modul Audit di luar cakupan TAG; elemen dialog Report TAG (opsi "QR", Report Type, Textarea "Note") ditulis persis seperti di TC.
  - Pernyataan QR-00232 tetap Paired pada Expected butir b tidak punya langkah observasi di TC selain tab To Be Returned; spec membacanya lewat fixture BE.
