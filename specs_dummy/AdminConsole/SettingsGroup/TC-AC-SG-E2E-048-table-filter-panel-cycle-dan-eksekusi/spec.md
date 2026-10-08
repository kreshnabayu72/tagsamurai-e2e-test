---
id: TC-AC-SG-E2E-048-table-filter-panel-cycle-dan-eksekusi
title: "Eksekusi filter panel tabel utama: range Min-Max, Modified By, Last Updated, dan siklus Clear Field tanpa auto-reset"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-92
  - TC-AC-SG-93
  - TC-AC-SG-160
  - TC-AC-SG-177
  - TC-AC-SG-196
coverage:
  web: automated
---

# Eksekusi filter panel tabel utama: range Min-Max, Modified By, Last Updated, dan siklus Clear Field tanpa auto-reset

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat data group dengan variasi Total User/Member, nama Modified By, dan tanggal Last Updated

## Test Steps

### Screening & Eksekusi Filter Panel
1. Klik tombol `[Filter]` pada toolbar tabel utama untuk membuka panel filter
2. Buka dropdown filter Modified By
3. Verifikasi opsi dropdown terisi dinamis hanya dari nama-nama user yang genuinely pernah memodifikasi group entitas ini
4. Masukkan range Total User (Min: 1, Max: 10)
5. Pilih salah satu nama pada filter Modified By
6. Pada field Last Updated, pilih 1 tanggal spesifik via date picker
7. Klik tombol `[Apply]`
8. Verifikasi tabel utama tersaring menampilkan baris yang memenuhi kombinasi ketiga filter tersebut
### Siklus Clear Field Tanpa Auto-Reset
9. Buka kembali Filter Panel yang masih menyimpan parameter aktif
10. Klik tombol `[Clear Field]`
11. Verifikasi seluruh field input di filter panel menjadi kosong/reset
12. Amati baris pada tabel utama di belakang panel
13. Verifikasi tabel utama BELUM me-reset datanya (data tidak boleh berubah sebelum tombol Apply ditekan)
14. Klik tombol `[Apply]`
15. Verifikasi tabel utama baru me-reset tampilannya dan menampilkan seluruh data semula

## Notes

- Clear Field hanya mereset form filter lokal; perubahan pada tabel memerlukan eksekusi Apply eksplisit.
