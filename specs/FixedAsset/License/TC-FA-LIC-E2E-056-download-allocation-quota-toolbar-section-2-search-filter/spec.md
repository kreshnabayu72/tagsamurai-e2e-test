---
id: TC-FA-LIC-E2E-056-download-allocation-quota-toolbar-section-2-search-filter
title: "Download Allocation Quota: Toolbar Section 2, Mengikuti Search dan Filter, serta Seluruh Baris yang Cocok"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-550
  - TC-FA-LIC-553
  - TC-FA-LIC-554
  - TC-FA-LIC-555
coverage:
  web: automated
---

# Download Allocation Quota: Toolbar Section 2, Mengikuti Search dan Filter, serta Seluruh Baris yang Cocok

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #12 (hanya dibaca kecuali langkah 34): hierarki PT Sejahtera dengan grup level 1 Produksi (`GRP-PRD`, Allocated Quota 1500), Cabang Medan (`GRP-MDN`, 1000, Used 880, Remaining 120), Cabang Surabaya (800), dan Kantor Pusat (1500) yang memiliki Divisi Logistik, Divisi IT, dan Divisi Keuangan; Unallocated Pool 200; lewat `Fixture.fixedAssetLicense.kuotaHierarki` (fixture belum ada; disediakan tim FE/BE).
- Data Dinamis (langkah 34, TC-FA-LIC-555): delapan grup level 1 tambahan bernama `Grup Uji <n> {runId}-056` (n = 1 sampai 8), masing-masing Allocated Quota 20 (jumlah 160, di bawah Unallocated Pool 200), sehingga total 12 grup level 1. Dibuat oleh fixture BE pada langkah 34 (disediakan tim FE/BE) dan dihapus di hook `after`; menambah entri Changelog, System Log, dan Activity Log di tenant uji. Kasus lain di spec ini memakai empat grup level 1 Pre-setup.
- Kemampuan teknis: mengirim tombol `Esc` untuk menutup popover (langkah 5 dan 10).
- Kemampuan teknis (dinyatakan di `suite.md`, dirujuk satu baris): membaca isi berkas unduhan CSV (nama berkas, baris, sel); berkas tiap unduhan ditangkap ke direktori bersih; fixture BE pemulih Pre-setup #12 dijalankan di hook `before` dan `after`.
- State yang diubah dan dipulihkan: Search dan Filter Section 2 (dibersihkan pada langkah 25 dan 32).

## Test Steps

### TC-FA-LIC-550: Toolbar Section 2 dan popover Download

1. Klik Tab `Allocation Quota`
2. Verifikasi toolbar Section 2 `Level 1 Groups Quota` berurutan `Search | Filter | Download | Changelog`
3. Klik ikon Download pada toolbar Section 2
4. Verifikasi popover menampilkan `Download as CSV` dan `Download as XLSX`
5. Tekan Esc untuk menutup popover
6. Klik node `Kantor Pusat` di Sidebar
7. Verifikasi toolbar Section 2 `Child Groups Quota` berurutan `Search | Filter | Download | Changelog`
8. Klik ikon Download pada toolbar Section 2
9. Verifikasi popover node Kantor Pusat menampilkan `Download as CSV` dan `Download as XLSX`
10. Tekan Esc untuk menutup popover

### TC-FA-LIC-553: Download mengikuti Search aktif Section 2

11. Klik node `All Groups` di Sidebar
12. Ketik Search `Medan` pada Search toolbar Section 2, tekan Enter
13. Verifikasi tabel Section 2 menampilkan satu baris: Cabang Medan
14. Klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
15. Verifikasi baris 1 berkas adalah header `License,Asset,+ Audit,+ Tracking,+ Maintenance Routine,+ Repair Ticketing,+ Maps,+ IT Inventory`
16. Verifikasi baris 2 berkas `Total,5000,100,50,30,30,Not Available,200`
17. Verifikasi baris 3 berkas `Used,4320,60,48,12,12,-,120`
18. Verifikasi baris 4 berkas `Reserved,15,-,-,-,-,-,-`
19. Verifikasi baris 5 berkas `Remaining,665,40,2,18,18,-,80`
20. Verifikasi baris 6 berkas `Unmanaged,27,-,-,-,-,-,-`
21. Verifikasi baris 7 berkas kosong
22. Verifikasi baris 8 berkas adalah header `Group Name,Group Code,Allocated Quota,Allocated to Subgroups,Used by This Group,Reserved by This Group,Remaining Quota,+ Audit,+ Tracking,+ Maintenance Routine,+ Repair Ticketing,+ Maps,+ IT Inventory`
23. Verifikasi baris 9 berkas `Cabang Medan,GRP-MDN,1000,0,880,0,120,15,10,3,3,-,25`
24. Verifikasi berkas tidak memiliki baris 10
25. Klik `(←)` pada kotak Search Section 2

### TC-FA-LIC-554: Download mengikuti Filter aktif Section 2

26. Buka Filter Panel Section 2, isi `Allocated Quota` Min `1000` dan Max `1500`, lalu klik `[Apply]`
27. Verifikasi tabel Section 2 menampilkan tiga baris: Produksi, Cabang Medan, Kantor Pusat
28. Klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
29. Verifikasi blok Section 1 pada berkas memuat lima baris penuh
30. Verifikasi blok Section 2 setelah baris kosong dan header memuat tiga baris data Produksi, Cabang Medan, Kantor Pusat
31. Verifikasi Cabang Surabaya (800) tidak ada pada berkas
32. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-LIC-555: Download memuat seluruh baris yang cocok

33. Verifikasi tabel Section 2 menampilkan empat baris sebelum fixture ditambahkan
34. Tambahkan delapan grup level 1 `Grup Uji <n> {runId}-056` beralokasi 20 per grup lewat fixture BE hingga tersimpan, lalu muat ulang halaman (F5)
35. Verifikasi halaman 1 Section 2 menampilkan 10 dari 12 baris
36. Klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
37. Verifikasi blok Section 2 pada berkas memuat 12 baris data (satu per grup level 1), bukan 10

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Urutan TC dalam spec: 550, 553, 554, 555 (kasus yang menambah grup di akhir). Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec di atas 35 langkah (37 langkah). Alasan: seluruh blok satu topik (Download Allocation Quota Section 2) pada dataset Pre-setup #12 yang hanya dibaca, dan tiap blok berdiri sendiri; langkah tambahan berasal dari satu `Verifikasi` per baris berkas pada Expected TC-FA-LIC-553 (S-01).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (membuka Tab `Allocation Quota`; node `All Groups` aktif saat tab pertama kali dibuka), langkah 5 dan 10 (menutup popover dengan Esc), langkah 11 (kembali ke node `All Groups`), langkah 14, 28, dan 36 (membuka isi berkas), langkah 25 dan 32 (pemulihan Search dan Filter; S-09), langkah 34 (seeding delapan grup; nilai kuota 20 per grup dari TC).
- Asersi di luar Expected TC (S-03): langkah 33 (empat baris sebelum penambahan) adalah anchor perbandingan untuk asersi 10 dari 12 baris pada langkah 35.
- P-10 (isi berkas pada spec fungsional, bagian 3 prinsip 13f): spec ini mengasersi nama berkas, baris header, dan jumlah baris sebagai asersi fungsional. Langkah 15 sampai 20 dan 23 mengasersi nilai sel berkas karena Expected TC-FA-LIC-553 menuliskannya; asersi nilai sel lain ada di spec 058.
- Temuan untuk QA:
  - TC-FA-LIC-555 tidak menyebut cara menyiapkan delapan grup tambahan selain "fixture"; mekanismenya disediakan tim FE/BE (S-13).
  - TC-FA-LIC-550, 553, 554, dan 555 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
