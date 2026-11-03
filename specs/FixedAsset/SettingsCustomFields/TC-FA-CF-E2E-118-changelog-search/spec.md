---
id: TC-FA-CF-E2E-118-changelog-search
title: "Modal Changelog: Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-455
  - TC-FA-CF-458
  - TC-FA-CF-459
  - TC-FA-CF-460
  - TC-FA-CF-461
  - TC-FA-CF-462
coverage:
  web: automated
---

# Modal Changelog: Search

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Changelog (Pre-setup #19) dengan email mengikuti pola Pre-setup #1 `totalControl_automated_{namaCompany}@qwertysystem.net` dan `{namaCompany}` = Company Changelog (email akun ini tidak tertulis di Pre-setup TC, lihat Temuan untuk QA). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_CHANGELOG_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_CHANGELOG_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Data Pre-setup (tetap di environment, tidak diubah spec ini): Company Changelog (Pre-setup #19; Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Jakarta) dengan dua belas entri Changelog tab General dan dua entri Create tab Purchasing, dirujuk lewat fixture baru `Fixture.faCustomFields.changelogSeed` (fixture belum ada, disediakan tim FE). Seed dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE). Entri seed yang dipakai Search (kolom Action | Field Name | Field | Old Value | New Value | Modified By):
  - `Bulk Delete` | `Old Field B` | `Name` | `Old Field B` | `—` | `Joko W`
  - `Edit` | `Legacy Tag` | `Placeholder` | `—` | `Enter legacy tag` | `Joko W`
  - `Edit` | `Operating Voltage` | `Global Value` | `Generator: 200V` | `Generator: 220V` | `Budi S`
  - `Edit` | `Equipment Class` | `Dropdown Options` | `Class A, Class B` | `Class A, Class B, Class C` | `Siti A` (Siti Amelia)
  - `Activate`, `Deactivate`, `Delete` (`Old Field`), `Edit`, dan `Create` pada entri seed lain (`Equipment Class`, `Total Cost`, `Old Field`, `Asset Serial Tag`)
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data dan tidak menambah entri Changelog.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan isi baris tabel Modal Changelog dan fokus input Search.
- State global: tidak ada yang diubah.

## Test Steps

1. Klik icon Changelog di toolbar

### TC-FA-CF-458: Search Modal Changelog: reveal, fokus, placeholder, dan submit dengan Enter

2. Klik icon Search di toolbar modal
3. Verifikasi input melebar dengan fokus otomatis
4. Verifikasi placeholder `Search action, field name...`
5. Ketik `Storage` pada kotak Search tanpa menekan Enter
6. Verifikasi tabel belum tersaring (entri `Asset Serial Tag` masih tampil)
7. Tekan Enter
8. Verifikasi tabel tersaring menampilkan entri `Storage Capacity`
9. Verifikasi tidak ada entri selain `Storage Capacity` pada tabel

### TC-FA-CF-459: Search kelas teks mencocokkan Action, Field Name, Field, Old Value, dan New Value

10. Ganti isi kotak search dengan `bulk`, tekan Enter
11. Verifikasi `bulk` menemukan baris `Bulk Delete`
12. Ganti isi kotak search dengan `placeholder`, tekan Enter
13. Verifikasi `placeholder` menemukan baris Edit Placeholder `Legacy Tag`
14. Ganti isi kotak search dengan `200v`, tekan Enter
15. Verifikasi `200v` menemukan baris Global Value dengan Old Value `Generator: 200V`
16. Ganti isi kotak search dengan `Class C`, tekan Enter
17. Verifikasi `Class C` menemukan baris Dropdown Options dengan New Value `Class A, Class B, Class C`

### TC-FA-CF-460: Search memakai pencocokan substring sehingga kata yang menjadi bagian kata lain ikut ditemukan

18. Ganti isi kotak search dengan `activate`, tekan Enter
19. Verifikasi `activate` menemukan baris `Activate`
20. Verifikasi `activate` menemukan baris `Deactivate`
21. Ganti isi kotak search dengan `delete`, tekan Enter
22. Verifikasi `delete` menemukan baris `Delete`
23. Verifikasi `delete` menemukan baris `Bulk Delete`

### TC-FA-CF-461: Search kolom Modified By Changelog mencocokkan nama lengkap user

24. Ganti isi kotak search dengan `amelia`, tekan Enter
25. Verifikasi baris dengan Modified By `Siti A` (nama lengkap Siti Amelia) ditemukan

### TC-FA-CF-462: Kolom Date tidak dapat dicari lewat Search

26. Ganti isi kotak search dengan `17/10/26`, tekan Enter
27. Verifikasi tidak ada baris yang ditemukan (empty state tampil)

### TC-FA-CF-455: Search pada Changelog tanpa hasil menampilkan empty state filtered

28. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
29. Verifikasi ilustrasi dengan Title `No results found` dan Description `Try adjusting your search or filter.` tampil
30. Klik `(←)` pada kotak Search
31. Klik icon `[✕]` untuk menutup modal

## Notes

- Spec memuat 31 langkah, di bawah ambang sekitar 35 langkah. Satu topik (Search Modal Changelog), satu akun, satu dataset (Company Changelog) tanpa mengubah data.
- Urutan TC di spec: 458, 459, 460, 461, 462, 455. TC-FA-CF-455 (empty state) dan TC-FA-CF-462 (tanpa hasil) berada di akhir supaya Search berhasil dahulu dan state kosong tidak menjadi keadaan awal TC lain (S-10). Langkah uji TC-FA-CF-455 ("Klik icon Search", "Cari `zzzxxx`") dijalankan pada kotak Search yang sudah terbuka (langkah 28).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka modal sesuai langkah uji TC), langkah 30 (`(←)` menutup kotak Search dan mereset tabel), langkah 31 (menutup modal). Search pada TC ini adalah objek uji.
- Absence langkah 9 didahului langkah 8 (entri `Storage Capacity` tampil); absence langkah 27 memakai empty state hasil Search sebagai anchor (bagian 8b butir 2).
- Temuan untuk QA:
  - Email akun Total Control Company Changelog tidak tertulis di Pre-setup TC; spec memakai pola Pre-setup #1, dan akunnya disediakan tim FE.
  - TC-FA-CF-458 Expected b ("Tabel tersaring hanya setelah Enter menjadi entri `Storage Capacity`") bermajemuk; spec memecahnya menjadi tabel belum tersaring sebelum Enter, tersaring menjadi `Storage Capacity` setelah Enter, dan tidak ada entri lain.
  - TC-FA-CF-460 Expected a dan b ("menemukan baris `Activate` dan `Deactivate`") dipecah menjadi satu `Verifikasi` per baris (S-01).
  - TC-FA-CF-462 Expected ("Tidak ada baris yang ditemukan") tidak menyebut teks empty state; spec memeriksa empty state tampil tanpa teks.
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
