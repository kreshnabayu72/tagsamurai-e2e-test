---
id: TC-GS-GSET-E2E-027-changelog-screening-urutan-default-tooltip-backdrop-dan-fokus
title: "Modal Changelog: Screening, Urutan Default, Tooltip, Klik Backdrop, dan Fokus Keyboard"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-60
  - TC-GS-GSET-65
  - TC-GS-GSET-85
  - TC-GS-GSET-86
  - TC-GS-GSET-96
coverage:
  web: automated
---

# Modal Changelog: Screening, Urutan Default, Tooltip, Klik Backdrop, dan Fokus Keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak mengganti sesi. Halaman General Settings dibuka di hook `beforeEach`. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Seeding minimal (S-11, S-12; hook `before`, sesudah record Client A berada di baseline Pre-setup baris 10), lewat `PUT /v2/enterprise-management/general-settings` (`global-settings/general-settings/API/openapi.yaml`) oleh sesi API akun Budi Santoso, payload mengacu ke `Fixture.generalSettings.payloadIdle60` dan `Fixture.generalSettings.payloadBaseline` (fixture belum ada; dibuat pada tahap script):
  - `PUT` pertama dengan `sessionIdleTimeout` 60 (nilai lain baseline): baris A (Field `Session Idle Timeout`, Old Value `30 minutes`, New Value `1 hour`, Modified By `Budi S`).
  - Hook menunggu sampai menit berganti (jeda maksimum 60 detik; konvensi bagian 6 untuk Date berketelitian menit, bukan langkah `Tunggu N detik` di spec).
  - `PUT` kedua dengan `sessionIdleTimeout` 30 (kembali ke baseline): baris B (Field `Session Idle Timeout`, Old Value `1 hour`, New Value `30 minutes`, Modified By `Budi S`).
  - Baris A dan B adalah baris terbaru sehingga tampil di halaman pertama; Date keduanya berbeda pada menit (dipakai sebagai pembanding urutan di langkah 21).
- Changelog General Settings adalah audit trail permanen; asersi spec memakai pola baris, tidak pernah jumlah entri absolut (S-12). Entri tidak dihapus.
- Kemampuan teknis: hover ikon; menekan `Tab` dan `Esc`; membaca elemen yang sedang fokus.
- Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah): Modal Changelog ditutup; record Client A di baseline (hook suite).
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` dan pemulihan baseline record: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-GSET-85: Tooltip ikon Changelog di halaman dan ikon toolbar Modal Changelog

1. Hover icon Changelog di pojok kanan atas halaman
2. Verifikasi tooltip icon Changelog `Changelog`
3. Klik icon Changelog
4. Hover ikon Search di toolbar modal
5. Verifikasi tooltip `Search`
6. Hover ikon Filter di toolbar modal
7. Verifikasi tooltip `Filter`
8. Hover ikon Download di toolbar modal
9. Verifikasi tooltip `Download`

### TC-GS-GSET-60: Screening Modal Changelog: General Settings

10. Verifikasi bagian Header: Title `Changelog: General Settings`
11. Verifikasi bagian Header: Toolbar memuat ikon `Search | Filter | Download`
12. Klik icon Search di toolbar
13. Verifikasi bagian Header: placeholder Search `Search action, field, or value...`
14. Klik icon panah `(←)` untuk menutup Search
15. Verifikasi bagian Body: kolom `Date (sortable) | Action (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Actions (⋯)`
16. Verifikasi bagian Body: ikon sort kolom Date menunjukkan Newest First (urutan default Date descending)
17. Verifikasi bagian Body: kolom Modified By berformat `[first name lengkap] [huruf pertama last name]`, tampil `Budi S`
18. Verifikasi bagian Footer: Pagination default 10 baris per halaman

### TC-GS-GSET-65: Urutan default Changelog: Date descending

19. Verifikasi baris B (Field `Session Idle Timeout`, Old Value `1 hour`, New Value `30 minutes`) tampil
20. Verifikasi baris A (Field `Session Idle Timeout`, Old Value `30 minutes`, New Value `1 hour`) tampil
21. Verifikasi baris terurut Date descending (Newest First): baris B berada di atas baris A dan Date baris B lebih baru daripada Date baris A (berbeda pada menit)

### TC-GS-GSET-86: Klik backdrop tidak menutup Modal Changelog

22. Klik area backdrop di luar modal
23. Verifikasi Modal Changelog: General Settings tetap terbuka

### TC-GS-GSET-96: Accessibility Modal Changelog: focus trapped dan Esc menutup modal

24. Tekan `Tab` berulang melewati seluruh elemen fokusable modal (jumlah elemen fokusable di modal ditambah satu kali tekan)
25. Verifikasi fokus keyboard tetap berada di dalam modal (focus trapped)
26. Tekan `Esc`
27. Verifikasi Modal Changelog tertutup
28. Verifikasi fokus keyboard kembali ke halaman General Settings

## Notes

- Mode: FE+BE. Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-85, 60, 65, 86, 96. Alasan: TC-85 dimulai dari halaman sebelum modal dibuka dan menghasilkan modal terbuka untuk TC berikutnya; TC-60 dan 65 hanya mengamati; TC-86 tidak menutup modal; TC-96 menutup modal sehingga paling akhir (prinsip 6 bagian 3 konvensi). Modal Changelog dibuka sekali di langkah 3.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 12 (membuka input Search agar placeholder dapat diamati) dan 14 (menutup Search kembali ke icon). Langkah 24 menekan `Tab` sebagai aksi TC-96 langkah 2; jumlah tekan dihitung dari jumlah elemen fokusable agar fokus melewati seluruh elemen modal.
- Langkah 19 dan 20 `Verifikasi` baris A dan B tampil adalah pembanding sebelum asersi urutan di langkah 21 (S-11, bagian 8b butir 2); Expected TC-65 tidak memuatnya. Langkah 16 (indikator sort Newest First) memetakan butir "urutan default Date descending" pada Expected b TC-60, sedangkan urutan baris diasersi di langkah 21 (TC-65).
- Klausa "klik backdrop tidak menutup modal" pada Expected a TC-GS-GSET-60 diasersi di langkah 22 dan 23 (TC-GS-GSET-86); blok TC-GS-GSET-60 (langkah 10 sampai 18) tidak memuat langkah klik backdrop.
- Asersi memakai pola baris (bukan jumlah baris), sehingga entri Changelog dari run atau spec lain tidak memengaruhi hasil.
- Temuan untuk QA:
  - TC-GS-GSET-60 Expected a menyebut toolbar "Search (placeholder ...)" padahal placeholder hanya terlihat sesudah icon Search diklik (TC-GS-GSET-66); spec menambah klik icon Search dan penutupan Search sebagai langkah penghubung agar klausa placeholder dapat diasersi.
  - TC-GS-GSET-96 langkah 2 "Tekan Tab berulang melewati seluruh elemen modal" tidak menyebut jumlah tekan; spec menetapkannya dari jumlah elemen fokusable modal ditambah satu.
  - TC-GS-GSET-85 Expected b tidak menyebut posisi tooltip; hanya teksnya yang diasersi.
