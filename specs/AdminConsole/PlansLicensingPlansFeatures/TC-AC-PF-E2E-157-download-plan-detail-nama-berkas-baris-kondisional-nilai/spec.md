---
id: TC-AC-PF-E2E-157-download-plan-detail-nama-berkas-baris-kondisional-nilai
title: Download Plan Detail Nama Berkas, Baris Kondisional, dan Nilai API Call Quota
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-604
  - TC-AC-PF-605
  - TC-AC-PF-636
  - TC-AC-PF-647
coverage:
  web: automated
---

# Download Plan Detail Nama Berkas, Baris Kondisional, dan Nilai API Call Quota

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active.
- Data Pre-setup: Dataset Plan A (Pre-setup #21): default `Starter` (FAMS, Free, v2: Asset cap 25, Group count 1, Group hierarchy depth 1, Category count 5, Category hierarchy depth 1, Asset Name cap 10, seluruh Binary OFF, Feature Suites None, API call quota -) dan custom `Growth Tier` (v20: Group count 25, Group hierarchy depth 5, Category count 20, Category hierarchy depth 2, Asset Name cap 500, Asset ID Configuration ON, License allocation per group ON, Scheduled reports 1, Approval Workflow OFF, Borrowing Full, Assignment Basic, Transfer None, Disposal Basic, SAMP & Document Center OFF, Accounting & Depreciation None, Custom Report Builder OFF, Open API ON, API call quota 1M/month). Dataset Plan CQ (Pre-setup #51): custom plan `Paket Quota Kustom` (FAMS, Paid, v1, Open API ON, API call quota Custom `150000`). Dataset Plan CP (Pre-setup #53): custom plan `Paket Kuota Seratus` (API call quota 100000 lewat Custom) dan `Paket Kuota Sejuta` (1000000 lewat Custom), keduanya Open API ON.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Kemampuan membaca isi berkas CSV dan XLSX yang terunduh (encoding, BOM, pemisah, nama sheet, baris data) disediakan tim FE/BE. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup; form Edit ditutup tanpa perubahan.
- Kelas harness: f (binary buffer) untuk isi berkas.
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

### TC-AC-PF-604 Download Plan Detail default plan Free ke CSV

1. Klik Plan Name `Starter` untuk membuka Plan Detail.
2. Hover ikon Download pada header Plan Detail.
3. Verifikasi tooltip ikon `Download` tampil.
4. Klik ikon Download, pilih `Download as CSV`, lalu buka berkas CSV.
5. Verifikasi tidak ada toast sukses.
6. Verifikasi berkas CSV bernama `Plan-Detail-Starter.csv`.
7. Verifikasi header berkas dua kolom `Field` dan `Value`.
8. Verifikasi berkas berencoding UTF-8 dengan BOM dan berpemisah koma.
9. Verifikasi baris data berurutan identik Tab Overview (format berkas: `Version` bilangan bulat tanpa `v`, sel kosong `-`): `Plan Name` `Starter`; `Product` `FAMS`; `Pricing Type` `Free`; `Version` `2`; `TAG Features` `QR Only`; `Asset cap` `25`; `Group count` `1`; `Group hierarchy depth` `1`; `Category count` `5`; `Category hierarchy depth` `1`; `Asset Name cap` `10`; `Asset ID Configuration` `No`; `License allocation per group` `No`; `Scheduled reports` `-`; `Approval Workflow` `No`; `Borrowing` `None`; `Assignment` `None`; `Transfer` `None`; `Disposal` `None`; `SAMP & Document Center` `No`; `Accounting & Depreciation` `None`; `Custom Report Builder` `No`; `Open API` `No`; `API call quota` `-`.

### TC-AC-PF-605 Download Plan Detail custom plan ke XLSX

10. Klik segmen Breadcrumb `Plans & Features`, lalu klik tab Custom, lalu sub-tab Active, lalu klik Plan Name `Growth Tier` untuk membuka Plan Detail.
11. Klik ikon Download, pilih `Download as XLSX`, lalu buka berkas XLSX.
12. Verifikasi tidak ada toast sukses.
13. Verifikasi berkas XLSX bernama `Plan-Detail-Growth Tier.xlsx`.
14. Verifikasi berkas memuat satu sheet bernama `Sheet1` dengan header `Field` dan `Value`.
15. Verifikasi baris data berurutan: `Plan Name` `Growth Tier`; `Product` `FAMS`; `Version` `20`; `TAG Features` `All TAGs`; `Group count` `25`; `Group hierarchy depth` `5`; `Category count` `20`; `Category hierarchy depth` `2`; `Asset Name cap` `500`; `Asset ID Configuration` `Yes`; `License allocation per group` `Yes`; `Scheduled reports` `1`; `Approval Workflow` `No`; `Borrowing` `Full`; `Assignment` `Basic`; `Transfer` `None`; `Disposal` `Basic`; `SAMP & Document Center` `No`; `Accounting & Depreciation` `None`; `Custom Report Builder` `No`; `Open API` `Yes`; `API call quota` `1000000` (angka penuh tanpa satuan dan tanpa pemisah ribuan).
16. Verifikasi baris `Pricing Type` dan baris `Asset cap` tidak ada untuk custom plan.

### TC-AC-PF-636 API call quota kustom 150.000

17. Klik segmen Breadcrumb `Plans & Features`, lalu klik tab Custom, lalu sub-tab Active, lalu klik Plan Name `Paket Quota Kustom` untuk membuka Plan Detail.
18. Verifikasi baris API call quota di Tab Overview menampilkan `150,000/month`.
19. Klik ikon Download, pilih `Download as CSV`, lalu buka berkas CSV.
20. Verifikasi berkas `Plan-Detail-Paket Quota Kustom.csv` memuat baris `API call quota` bernilai `150000` (angka penuh tanpa pemisah ribuan dan tanpa satuan `/month`).

### TC-AC-PF-647 API call quota sama dengan preset

21. Klik segmen Breadcrumb `Plans & Features`, lalu klik tab Custom, lalu sub-tab Active, lalu klik Plan Name `Paket Kuota Seratus` untuk membuka Plan Detail.
22. Verifikasi baris API call quota di Tab Overview menampilkan `100K/month` (bukan `100,000/month`).
23. Klik ikon Download, pilih `Download as CSV`, lalu buka berkas CSV.
24. Verifikasi berkas `Plan-Detail-Paket Kuota Seratus.csv` memuat baris `API call quota` bernilai `100000` (angka penuh tanpa pemisah ribuan dan tanpa satuan).
25. Klik `Edit` di header Plan Detail.
26. Verifikasi field API call quota pada form Edit terpilih `100K/month`, bukan `Custom`.
27. Verifikasi input angka Custom tidak tampil.
28. Tutup form Edit tanpa mengubah apa pun (klik segmen Breadcrumb `Plans & Features`).
29. Klik tab Custom, lalu sub-tab Active, lalu klik Plan Name `Paket Kuota Sejuta` untuk membuka Plan Detail.
30. Verifikasi baris API call quota di Tab Overview menampilkan `1M/month` (bukan `1,000,000/month`).
31. Klik `Edit` di header Plan Detail.
32. Verifikasi field API call quota pada form Edit terpilih `1M/month`, bukan `Custom`.
33. Tutup form Edit tanpa mengubah apa pun (klik segmen Breadcrumb `Plans & Features`).

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 10, 17, dan 21 kembali ke Plans List lewat klik segmen Breadcrumb `Plans & Features` dari Plan Detail yang terbuka, lalu berpindah ke tab Custom dan membuka Plan Detail; langkah 29 berpindah ke tab Custom dan membuka Plan Detail; langkah 28 dan 33 menutup form Edit yang tidak dirty lewat klik segmen Breadcrumb `Plans & Features` (tanpa dialog `Unsaved Changes`).
- Verifikasi "tidak ada toast sukses" (langkah 5 dan 12) ditempatkan segera setelah pemicu download dan sebelum asersi berkas (bagian 8b butir 11).
- Anchor absence (bagian 8b butir 2): langkah 16 (baris `Pricing Type` dan `Asset cap` tidak ada) didahului langkah 15 yang membuktikan baris lain pada berkas yang sama ada.
- Temuan untuk QA: (1) TC-AC-PF-604 dan TC-AC-PF-605 mengasersi daftar baris berurutan sebagai satu Expected (butir d dan c) dengan nilai Version tanpa `v`; spec mengasersinya sebagai satu `Verifikasi` daftar utuh. (2) TC-AC-PF-605 menyebut `Growth Tier` v20 dengan atribut Dataset Plan A, sedangkan Dataset Plan C mendefinisikan `Growth Tier` v20 dengan Last Modified berbeda; spec memakai Dataset Plan A. (3) Dataset Plan CP tidak menyebut apakah Edit `Paket Kuota Seratus` menyimpan perubahan; spec menutup form tanpa perubahan.
- Jumlah langkah 33: di bawah ambang sekitar 35.
