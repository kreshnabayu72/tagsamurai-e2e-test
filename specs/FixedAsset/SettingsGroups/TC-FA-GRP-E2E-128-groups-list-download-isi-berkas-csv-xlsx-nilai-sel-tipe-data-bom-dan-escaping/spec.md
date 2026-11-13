---
id: TC-FA-GRP-E2E-128-groups-list-download-isi-berkas-csv-xlsx-nilai-sel-tipe-data-bom-dan-escaping
title: "Groups List Download Isi Berkas CSV/XLSX: Transformasi Tipe Badge, Number, Date, Empty, Function None/Modified By, BOM UTF-8 dan Escaping"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-412
  - TC-FA-GRP-413
  - TC-FA-GRP-414
  - TC-FA-GRP-415
  - TC-FA-GRP-422
  - TC-FA-GRP-1133
coverage:
  web: automated
---

# Groups List Download Isi Berkas CSV/XLSX: Transformasi Tipe Badge, Number, Date, Empty, Function None/Modified By, BOM UTF-8 dan Escaping

## Prerequisites

- Mode: FE+BE.
- Kelas harness: f (binary buffer) untuk isi berkas CSV/XLSX.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-128`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-128` | `V128L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-128` | `V128K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-128` | `V128J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-128` | `V128I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-128` | `V128H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-128` | `V128G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-128` | `V128F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-128` | `V128E` | None | 4 | 3 | ModB | 2 |
| `India {runId}-128` | `V128D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-128` | `V128C` | None | 7 | 7 | ModB | 2 |
| `Kilo {runId}-128` | `V128B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-128` | `V128A` | None | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-128`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): penangkapan berkas unduhan browser dan pembacaan isi berkas CSV/XLSX (nama berkas, baris header, jumlah baris data).
- Data Dinamis tambahan (suffix spec): group `Gudang, "Utama" {runId}-128` (level 1, Assignable) sebagai baris dengan koma dan tanda kutip pada nama; dibuat lewat API di `before` dan dihapus di `after`.

## Test Steps

1. Ketik Search `{runId}-128`, tekan Enter

### TC-FA-GRP-412, 413, 414, 415, 422: Isi sel berkas XLSX

2. Klik icon Download
3. Klik `Download as XLSX`
4. Verifikasi berkas `Groups.xlsx` terunduh
5. Buka berkas `Groups.xlsx`
6. Verifikasi kolom badge (Function) ditulis label teks apa adanya (`Assignable`) tanpa warna
7. Verifikasi kolom Total Asset dan Total User ditulis sebagai sel numerik asli
8. Verifikasi kolom Last Updated mengikuti format tanggal General Settings
9. Verifikasi nilai kosong Function `None` baris `bravo {runId}-128` ditulis hyphen tunggal `-` pada berkas
10. Verifikasi kolom Modified By baris `Alpha {runId}-128` sesuai nilai pada tabel

### TC-FA-GRP-1133: CSV UTF-8 BOM dan escaping, XLSX satu sheet, urutan mengikuti Sort aktif

11. Klik header Group dua kali sampai sort Descending
12. Klik icon Download
13. Klik `Download as CSV`
14. Verifikasi berkas `Groups.csv` terunduh
15. Buka berkas `Groups.csv` di editor teks
16. Verifikasi berkas `Groups.csv` diawali BOM UTF-8
17. Verifikasi nilai `Gudang, "Utama" {runId}-128` ter-escape (dibungkus tanda kutip, tanda kutip digandakan) sehingga tetap satu sel
18. Klik icon Download
19. Klik `Download as XLSX`
20. Verifikasi berkas `Groups.xlsx` terunduh
21. Buka berkas `Groups.xlsx`
22. Verifikasi berkas `Groups.xlsx` berisi satu sheet bernama `Sheet1`
23. Verifikasi urutan baris pada `Groups.csv` dan `Groups.xlsx` mengikuti Sort aktif (Group Z-A)
24. Klik header Group satu kali sampai sort netral
25. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Spec kelas f (isi berkas CSV/XLSX, bagian 3 prinsip 13). Nama berkas, header, dan jumlah baris diasersi pada spec 127.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka berkas unduhan dan mengembalikan sort ke netral (S-03).
- Baris Function `None` (`bravo`) dipakai sebagai nilai kosong untuk TC-FA-GRP-415 dan TC-FA-GRP-422; Modified By pada TC-FA-GRP-422 dibandingkan dengan nilai tabel (format `[First Name] [Last Initial]`, R-14).
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - TC-FA-GRP-1133 memakai group `Gudang, "Utama"` tanpa suffix; spec menambahkan suffix (bagian 5) sehingga nilai yang di-escape adalah `Gudang, "Utama" {runId}-128`.
