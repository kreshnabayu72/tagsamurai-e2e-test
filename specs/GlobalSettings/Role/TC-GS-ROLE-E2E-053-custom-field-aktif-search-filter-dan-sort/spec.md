---
id: TC-GS-ROLE-E2E-053-custom-field-aktif-search-filter-dan-sort
title: "Custom Field Aktif Dropdown: Search, Filter, dan Sort Kolom Region"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-146
coverage:
  web: automated
---

# Custom Field Aktif Dropdown: Search, Filter, dan Sort Kolom Region

## Prerequisites

- Mode: FE+BE.
- Akun aktor (login di hook `before`): Total Control, Ahmad Fauzi, `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), password `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD` (sudah terdaftar). Tidak ada env baru.
- Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control (Search, Filter, Sort, dan kolom tabel dalam keadaan bawaan).
- Custom Field aktif `Region` (tipe Dropdown, opsi `Jakarta` dan `Bandung`) tersedia dan dapat diisi pada user Total Control; disediakan tim FE (precondition TC-GS-ROLE-146).
- Data Dinamis milik spec (hook `before`, lewat seeding API): tiga user Total Control, Active, dengan nilai Region berbeda (S-11: dua nilai distinct pada kolom yang di-search, di-filter, dan di-sort):

| Nama | Email | Region |
|---|---|---|
| `Anggrek Uji {runId}-053` | `anggrekuji+{runId}-053@qwertysystem.net` | `Jakarta` |
| `Melati Uji {runId}-053` | `melatiuji+{runId}-053@qwertysystem.net` | `Bandung` |
| `Tulip Uji {runId}-053` | `tulipuji+{runId}-053@qwertysystem.net` | `Jakarta` |

- Urutan Name A-Z ketiga user: `Anggrek Uji`, `Melati Uji`, `Tulip Uji`. Urutan Region A-Z by label membuat `Melati Uji` (Bandung) berada di atas kedua user Jakarta; asersi sort membandingkan posisi relatif ketiga baris ini, tanpa menyatakan posisi baris Total Control lain yang Region-nya kosong.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): hapus tiga user di atas; kolom Region dikembalikan lewat `[Reset to Default]` (langkah 20 sampai 22); Search, Filter, dan Sort dibersihkan di dalam spec (langkah 10, 13, dan klik ketiga header Region).
- Kemampuan teknis: mengisi nilai Custom Field `Region` pada user lewat seeding API (disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD, tidak dikarang di spec); Popup Setup Column untuk menampilkan kolom; membaca posisi relatif baris tabel.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-GS-ROLE-146: Search, Filter, dan Sort Custom Field aktif bertipe Dropdown

1. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
2. Centang kolom Region
3. Klik `[Save]`
4. Klik Filter
5. Verifikasi field filter berlabel `Region` dengan placeholder `All regions`
6. Pada field Region pilih `Jakarta`
7. Klik `[Apply]`
8. Verifikasi baris `Anggrek Uji {runId}-053` dan `Tulip Uji {runId}-053` tampil
9. Verifikasi hanya baris ber-Region `Jakarta` yang tampil (baris `Melati Uji {runId}-053` tidak tampil)
10. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`
11. Ketik Search `jakarta`, tekan Enter
12. Verifikasi baris `Anggrek Uji {runId}-053` dan `Tulip Uji {runId}-053` (Region `Jakarta`) tampil (pencarian case-insensitive)
13. Klik `(←)` pada kotak Search
14. Klik header Region
15. Verifikasi Sort A-Z by label badge: baris `Melati Uji {runId}-053` (`Bandung`) berada di atas baris `Anggrek Uji {runId}-053` dan `Tulip Uji {runId}-053` (`Jakarta`)
16. Klik header Region
17. Verifikasi Sort Z-A: baris `Melati Uji {runId}-053` (`Bandung`) berada di bawah baris `Anggrek Uji {runId}-053` dan `Tulip Uji {runId}-053` (`Jakarta`)
18. Klik header Region
19. Verifikasi Sort kembali ke default Name A-Z: baris `Anggrek Uji {runId}-053`, `Melati Uji {runId}-053`, `Tulip Uji {runId}-053` berurutan
20. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
21. Klik `[Reset to Default]`
22. Klik `[Save]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Langkah penghubung (aksi tanpa `Verifikasi`): menampilkan kolom Region lewat Popup Setup Column (langkah 3), membersihkan filter (langkah 10; TC-GS-ROLE-146 Langkah 3), mengosongkan Search lewat `(←)` (langkah 13; Langkah 4), dan memulihkan kolom ke bawaan (langkah 20 sampai 22).
- Urutan klik header Region (tiga klik, satu `Verifikasi` tiap klik) memetakan Expected d: klik 1 A-Z, klik 2 Z-A, klik 3 default Name A-Z.
- Temuan untuk QA:
  - TC-GS-ROLE-146 tidak menyebut nilai Region, user yang diisi, atau nilai selain `Jakarta`; spec men-seed tiga user milik spec (dua `Jakarta`, satu `Bandung`) agar filter, search, dan sort punya sedikitnya dua nilai distinct (S-11).
  - TC-GS-ROLE-146 Expected d tidak menyebut posisi baris Total Control lain yang Region-nya kosong pada sort A-Z dan Z-A (kolom ini tidak punya klausa nilai kosong seperti TAG dan Temporary Until); spec hanya membandingkan posisi relatif tiga baris milik spec.
  - TC-GS-ROLE-146 Langkah 1 ("Tampilkan kolom Region") tidak menyebut Setup Column; spec memakai Popup Setup Column.
