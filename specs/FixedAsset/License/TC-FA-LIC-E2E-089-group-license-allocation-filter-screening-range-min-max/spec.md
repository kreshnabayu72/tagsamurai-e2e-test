---
id: TC-FA-LIC-E2E-089-group-license-allocation-filter-screening-range-min-max
title: "Group License Allocation: Filter Panel Screening, Range Min-Max per Kolom, dan Baris Bernilai Kosong"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-312
  - TC-FA-LIC-313
  - TC-FA-LIC-314
  - TC-FA-LIC-513
coverage:
  web: automated
---

# Group License Allocation: Filter Panel Screening, Range Min-Max per Kolom, dan Baris Bernilai Kosong

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Data Pre-setup #12 (data kuota dan hierarki PT Sejahtera, dipulihkan fixture BE di hook `before`): client Paid Pre-setup #1 dengan `License allocation per group` ON; hierarki Produksi, Kantor Pusat (Divisi Logistik, Divisi IT, Divisi Keuangan belum beralokasi `Allocated Quota —` dan `Remaining Quota —`), Cabang Surabaya, Cabang Medan. Tabel Group License Allocation pada node All Groups menampilkan empat baris level 1. Identitas dan nilai data dirujuk lewat `Fixture.fixedAssetLicense.kuotaHierarki` (belum ada, disiapkan tim FE); nilai pada langkah dan tabel di bawah adalah nilai fixture itu.
- Data Dinamis: tidak ada. Spec ini hanya membaca tabel.
- Tabel "Filter range Min-Max" (parameter langkah 19 sampai 24); `kosong` berarti field tidak diisi:

  | Field | Min | Max | Baris yang tampil |
  |---|---|---|---|
  | Allocated Quota | 1000 | 1500 | Produksi, Cabang Medan, Kantor Pusat |
  | Used by This Group | 800 | kosong | Produksi, Cabang Medan |
  | Reserved by This Group | 1 | 10 | Produksi, Cabang Surabaya |
  | Remaining Quota | kosong | 45 | Produksi, Cabang Surabaya |
  | Allocated to Subgroups | 1 | kosong | Kantor Pusat |
  | + Audit | 10 | 15 | Cabang Medan, Kantor Pusat |
  | + IT Inventory | 25 | 40 | Produksi, Cabang Medan |
  | + Tracking | 10 | 20 | Produksi, Cabang Medan |
  | + Maintenance Routine | 3 | 4 | Produksi, Cabang Medan |
  | + Repair Ticketing | 3 | 4 | Produksi, Cabang Medan |
  | + Maps | 1 | kosong | empty state `No results found` (nilai `—` tersaring keluar oleh filter range) |

- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih Pre-setup #12.

## Test Steps

### TC-FA-LIC-312: Screening Filter Panel, field, tipe komponen, label, dan placeholder

1. Klik tab Allocation Quota di node All Groups
2. Klik ikon Filter pada toolbar
3. Verifikasi ikon Filter berubah gelap
4. Verifikasi panel Filter tampil di bawah toolbar
5. Verifikasi field berurutan (maksimal 4 per baris): Allocated Quota, Allocated to Subgroups, Used by This Group, Reserved by This Group, Remaining Quota, + Audit, + Tracking, + Maintenance Routine, + Repair Ticketing, + Maps, + IT Inventory
6. Verifikasi field Allocated Quota: field range Min-Max, placeholder `Min` (input kiri) dan `Max` (input kanan)
7. Verifikasi field Allocated to Subgroups: field range Min-Max, placeholder `Min` (input kiri) dan `Max` (input kanan)
8. Verifikasi field Used by This Group: field range Min-Max, placeholder `Min` (input kiri) dan `Max` (input kanan)
9. Verifikasi field Reserved by This Group: field range Min-Max, placeholder `Min` (input kiri) dan `Max` (input kanan)
10. Verifikasi field Remaining Quota: field range Min-Max, placeholder `Min` (input kiri) dan `Max` (input kanan)
11. Verifikasi field + Audit: field range Min-Max, placeholder `Min` (input kiri) dan `Max` (input kanan)
12. Verifikasi field + Tracking: field range Min-Max, placeholder `Min` (input kiri) dan `Max` (input kanan)
13. Verifikasi field + Maintenance Routine: field range Min-Max, placeholder `Min` (input kiri) dan `Max` (input kanan)
14. Verifikasi field + Repair Ticketing: field range Min-Max, placeholder `Min` (input kiri) dan `Max` (input kanan)
15. Verifikasi field + Maps: field range Min-Max, placeholder `Min` (input kiri) dan `Max` (input kanan)
16. Verifikasi field + IT Inventory: field range Min-Max, placeholder `Min` (input kiri) dan `Max` (input kanan)
17. Verifikasi tombol `[Clear Field]` di kiri (text)
18. Verifikasi tombol `[Apply]` di kanan (filled)

### TC-FA-LIC-313 dan TC-FA-LIC-513: Filter per kelas field range Min-Max (inklusif, salah satu batas boleh kosong)

19. Untuk setiap baris tabel "Filter range Min-Max" (langkah 19 sampai 24): lihat field pada baris itu
20. Verifikasi placeholder input kiri `Min` dan input kanan `Max` pada field itu
21. Isi Min dan Max field pada baris itu (kosongkan input bila nilainya `kosong`)
22. Klik `[Apply]`
23. Verifikasi tabel menampilkan tepat hasil pada kolom "Baris yang tampil" untuk baris tabel itu
24. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-LIC-314: Filter range pada kolom kuota, baris bernilai `—` tersaring keluar

25. Klik ikon Filter untuk menutup panel
26. Klik node `Kantor Pusat` pada Sidebar
27. Buka Filter Panel, isi `Allocated Quota` Min `0`, klik `[Apply]`
28. Verifikasi Divisi Logistik dan Divisi IT tampil
29. Verifikasi Divisi Keuangan (Allocated `—`) tidak tampil
30. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah penghubung tanpa `Verifikasi`: `[Clear Field]` lalu `[Apply]` di akhir tiap iterasi dan di akhir TC-FA-LIC-314 (S-09), menutup Filter Panel sebelum berpindah node (langkah 25), serta membuka node `Kantor Pusat` pada TC-FA-LIC-314. Filter Panel tetap terbuka sesudah `[Apply]` (prd-conventions.md §9.8), sehingga iterasi berikutnya tidak membuka panel lagi.
- Blok ulang: langkah 19 sampai 24 dijalankan 11 kali (7 field TC-FA-LIC-313 dan 4 field TC-FA-LIC-513). Spec di atas 35 langkah (30 langkah nominal; 90 langkah setelah ekspansi). Alasan: seluruh blok adalah Filter satu tabel dengan satu dataset Pre-setup #12 dan satu kelas harness, dan kegagalan satu field tidak membuat field lain kehilangan makna.
- Asersi di luar Expected TC (S-03): `Verifikasi` placeholder `Min` (input kiri) dan `Max` (input kanan) pada langkah 20 berasal dari Expected a TC-FA-LIC-313 untuk tujuh field; untuk empat field TC-FA-LIC-513 (`+ Tracking`, `+ Maintenance Routine`, `+ Repair Ticketing`, `+ Maps`) langkah yang sama diulang karena langkah loop tanpa percabangan, dengan klausa yang sama seperti TC-FA-LIC-312.
- Temuan untuk QA: TC-FA-LIC-313 data Reserved by This Group `1–10` dan Remaining Quota `None–45` dibaca sebagai salah satu batas kosong. TC-FA-LIC-312, 313, 314, dan 513 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
