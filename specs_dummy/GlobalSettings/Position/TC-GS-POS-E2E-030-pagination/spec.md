---
id: TC-GS-POS-E2E-030-pagination
title: Pagination — Default, Page Size 25/50/100, Next/Prev, Refresh Pertahankan State, Navigasi
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-30
  - TC-GS-POS-32
  - TC-GS-POS-245
coverage:
  web: automated
---

# Pagination — Default, Page Size 25/50/100, Next/Prev, Refresh Pertahankan State, Navigasi

## Prerequisites

- Aktor `Fixture.globalSettingsPosition.actors.totalControl`.
- Total Position aktif ≥100 (population/seed) agar opsi 100 benar-benar teruji.
- Tabel memiliki kontrol paginasi (Prev/Next, nomor halaman, page size overlay).
- Konvensi §9.11: Default 10/halaman, opsi 10/25/50/100, 100 maksimum, tidak ada "All".

## Test Steps

### A. Default & opsi

1. Buka halaman tanpa filter/search khusus (kondisi default).
2. Verifikasi page size default = 10 baris per halaman.
3. Buka overlay Page Size.
4. Verifikasi opsi tersedia: 10, 25, 50, 100.
5. Verifikasi kontrol Prev/Next ada dan status disabled sesuai posisi halaman.
6. Verifikasi nomor halaman aktif ter-highlight.

### B. Page Size 25/50/100

7. Ubah page size ke 25.
8. Verifikasi tepat 25 baris tampil dalam 1 halaman (jika data ≥25).
9. Ubah page size ke 50.
10. Verifikasi tepat 50 baris tampil (jika data ≥50).
11. Ubah page size ke 100.
12. Verifikasi tepat 100 baris tampil (jika data ≥100), dan 100 adalah maksimum tanpa opsi "All".
13. Verifikasi tidak ada duplikasi/menghilang baris; total dataset dan info pagination konsisten.
14. Kembalikan page size ke 10.

### C. Navigasi Next/Prev & antar halaman

15. Pastikan berada di halaman 1 dengan page size 10 (dan total ≥11).
16. Klik `Next`.
17. Verifikasi data berpindah ke halaman 2, tidak ada duplikasi/row hilang.
18. Klik `Prev`.
19. Verifikasi kembali ke halaman 1 dengan data yang benar.

### D. Refresh mempertahankan state

20. Pindah ke halaman 2.
21. Terapkan sort Last Updated Desc (atau sort aktif lain yang mudah diamati).
22. Refresh browser (F5).
23. Verifikasi halaman tetap di halaman 2.
24. Verifikasi sort tetap Last Updated Desc (state dipertahankan).
25. Kembali ke kondisi netral jika diperlukan.

## Notes

- Langkah 8–12 menegaskan jumlah baris persis sesuai pilihan page size.
- D menegaskan preservasi state paginasi+sort setelah refresh (sesuai §27.1c lintas referensi), bukan reset.
