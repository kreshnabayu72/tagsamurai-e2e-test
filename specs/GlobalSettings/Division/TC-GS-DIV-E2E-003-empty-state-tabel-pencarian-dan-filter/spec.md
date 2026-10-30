---
id: TC-GS-DIV-E2E-003-empty-state-tabel-pencarian-dan-filter
title: "Empty State Tabel Division: Search dan Filter Tanpa Hasil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-6
  - TC-GS-DIV-7
coverage:
  web: automated
---

# Empty State Tabel Division: Search dan Filter Tanpa Hasil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup Division (6 Division, data environment tetap; hanya dibaca): Finance, Human Resources, Legal, Operations, Compliance, Treasury. Last Updated semua Division lebih baru dari 31-01-2020 sehingga rentang Filter pada TC-GS-DIV-7 tidak mencocokkan baris mana pun. Spec tidak membuat atau mengubah data backend.
- Data uji: keyword Search `zzzzqq` (TC-GS-DIV-6); Filter Last Updated 01-01-2020 sampai 31-01-2020 (TC-GS-DIV-7).
- Guided Tooltip: hook `before` mencatat nilai awal flag `guided_tooltip_seen_gs-division` lalu menyetelnya ke true; hook `after` memulihkan nilai awal. Kemampuan membaca dan menyetel flag disediakan tim FE/BE (nama endpoint tidak disebut di TC dan PRD).
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- State global yang diubah: hanya flag Guided Tooltip (dipulihkan seperti di atas). State Search dan Filter tabel dibersihkan lewat langkah pemulihan di tengah dan di akhir spec.

## Test Steps

### TC-GS-DIV-6: Empty state tabel saat Search tidak menemukan hasil

1. Klik icon Search
2. Ketik `zzzzqq` pada kotak Search
3. Tekan Enter
4. Verifikasi tabel menampilkan Illustration (100x100)
5. Verifikasi Title `No results found`
6. Verifikasi Description `Try adjusting your search or filter.`
7. Hapus keyword Search sehingga tabel kembali menampilkan Division

### TC-GS-DIV-7: Empty state tabel saat Filter Last Updated tidak menemukan hasil

8. Klik icon Filter
9. Pilih Last Updated rentang 01-01-2020 sampai 31-01-2020
10. Klik `[Apply]`
11. Verifikasi tabel menampilkan Illustration (100x100)
12. Verifikasi Title `No results found`
13. Verifikasi Description `Try adjusting your search or filter.`
14. Reset Filter Last Updated sehingga tabel kembali menampilkan Division

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 7 (hapus keyword Search supaya TC-GS-DIV-7 berasal dari Filter saja) dan 14 (reset Filter Last Updated).
- Temuan untuk QA:
  - TC-GS-DIV-7 menulis rentang tanggal `01-01-2020` sampai `31-01-2020` sementara langkah menyebut contoh `1 Jan 2020`; format input tanggal mengikuti General Settings dan tidak dinyatakan di TC. Spec memakai nilai Data Uji `01-01-2020` sampai `31-01-2020`.
