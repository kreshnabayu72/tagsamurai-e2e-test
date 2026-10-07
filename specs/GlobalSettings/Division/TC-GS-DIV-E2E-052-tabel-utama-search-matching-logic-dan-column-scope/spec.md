---
id: TC-GS-DIV-E2E-052-tabel-utama-search-matching-logic-dan-column-scope
title: "Pencarian Tabel Utama: Pencocokan Substring Name & Code, Case-Insensitive, Empty State, dan Scoping Kolom Tersembunyi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-144
  - TC-GS-DIV-145
  - TC-GS-DIV-146
  - TC-GS-DIV-147
  - TC-GS-DIV-148
coverage:
  web: automated
---

# Pencarian Tabel Utama: Pencocokan Substring Name & Code, Case-Insensitive, Empty State, dan Scoping Kolom Tersembunyi

## Prerequisites

- Login sebagai Role: Total Control
- Tabel terisi data divisi variasi (TC-GS-DIV-30)
- User berada di Global Settings > User > Division
- Tabel Division terisi 32 baris (TC-GS-DIV-30)

## Test Steps

### Search per kolom searchable: Name dan Code (substring dan tanpa membedakan huruf besar kecil) (TC-GS-DIV-144)

1. Cari `ACCOUN` (potongan Name) lalu Enter
2. Cari `accounting` (huruf kecil) lalu Enter
3. Cari `QA` (Code Quality Assurance) lalu Enter
4. Cari `qa` (huruf kecil) lalu Enter
5. Verifikasi Kolom Name: keyword `ACCOUN` dan `accounting` menemukan baris `Accounting`
6. Verifikasi Kolom Code: keyword `QA` dan `qa` menemukan baris `Quality Assurance` (Code `QA`)

### Last Updated tidak dapat dicari lewat Search toolbar (TC-GS-DIV-145)

7. Lihat nilai Last Updated salah satu baris dalam format yang tampil
8. Ketik nilai tanggal tersebut pada Search lalu Enter
9. Verifikasi Tabel menampilkan `No results found` (Last Updated bukan kolom searchable)
10. Verifikasi Penyaringan tanggal hanya lewat Filter Panel

### Search tidak mencari kolom yang di-hide (TC-GS-DIV-146)

11. Buka Overlay Column Visibility dan hilangkan centang kolom `Code`
12. Cari `QA` lalu Enter
13. Cari `Quality` lalu Enter
14. Verifikasi Keyword `QA` tidak menemukan baris `Quality Assurance` lewat kolom Code yang di-hide
15. Verifikasi Keyword `Quality` tetap menemukan baris `Quality Assurance` lewat kolom Name

### Search kembali mencari kolom setelah di-unhide (TC-GS-DIV-147)

16. Hilangkan centang kolom `Code`, lalu centang kembali kolom `Code`
17. Cari `QA` lalu Enter
18. Verifikasi Keyword `QA` kembali menemukan baris `Quality Assurance` lewat kolom Code

### Search dari halaman lebih dari 1 mereset ke halaman 1 (TC-GS-DIV-148)

19. Pindah ke halaman 3 tabel
20. Klik icon Search, ketik `a`, tekan Enter
21. Verifikasi Tabel kembali ke halaman 1 dengan hasil search

## Notes

- Memvalidasi logika pencocokan pencarian: pencarian Name dan Code secara case-insensitive (NC-06), pencocokan partial substring, empty state saat tidak ada hasil cocok, reset ke halaman 1, dan kolom yang disembunyikan via Setup Column tidak disertakan dalam pencarian (PRD §4.1.1, §4.4, §5).
- Sumber pemetaan test case granular: TC-GS-DIV-144, TC-GS-DIV-145, TC-GS-DIV-146, TC-GS-DIV-147, TC-GS-DIV-148.
