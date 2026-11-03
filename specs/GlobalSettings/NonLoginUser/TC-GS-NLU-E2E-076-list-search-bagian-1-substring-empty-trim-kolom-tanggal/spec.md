---
id: TC-GS-NLU-E2E-076-list-search-bagian-1-substring-empty-trim-kolom-tanggal
title: "List Search bagian 1: substring tanpa membedakan huruf besar kecil, empty state, pemangkasan spasi dan karakter khusus, kolom tanggal Last Update"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-257
  - TC-GS-NLU-258
  - TC-GS-NLU-260
  - TC-GS-NLU-261
coverage:
  web: automated
---

# List Search bagian 1: substring tanpa membedakan huruf besar kecil, empty state, pemangkasan spasi dan karakter khusus, kolom tanggal Last Update

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1; `{namaCompany}` diisi sesuai Client uji). Login sekali di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password lewat `Spectra.env.GS_TC_PASSWORD`, tidak ditulis di spec atau fixture.
- Layar awal: Global Settings > User > User List > sub-tab Non-Login User, dibuka hook `beforeEach` suite.
- Data Pre-setup (No. 9 sampai 12; hanya dibaca, tidak diubah, tanpa suffix): Non-Login User `Budi Kurniawan` (Field Technician, Operations, `FT-0231`, Represented By Ahmad Fauzi), `Siti Rahayu` (Warehouse, tanpa Position dan Employee ID), `Rina Marlina` (Driver, Logistics, Temporary), `Agus Salim` dan `Joko Susilo` (Contractor, Inactive). Fixture baru `Fixture.nonLoginUser.preSetup` (belum ada).
- Data Dinamis: tidak ada. Spec ini tidak menulis atau menghapus data.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-non-login-user` true untuk akun Total Control dan hook suite `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pengamatan dialog browser (untuk memastikan tidak ada `alert` pada langkah 16); pembacaan nilai sel Last Update dari tabel.
- State global: tidak ada yang diubah. State tabel (Search) dikosongkan oleh langkah penghubung di akhir tiap TC. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-257: Search substring dan case-insensitive pada kolom Name, Position, Division, Employee ID, Represented By

1. Ketik Search `rahayu`, tekan Enter
2. Verifikasi baris `Siti Rahayu` ditemukan (kolom Name, substring, tidak membedakan huruf besar kecil)
3. Ganti isi kotak search dengan `TECHNIC`, tekan Enter
4. Verifikasi baris `Budi Kurniawan` ditemukan (kolom Position, substring, tidak membedakan huruf besar kecil)
5. Ganti isi kotak search dengan `operat`, tekan Enter
6. Verifikasi baris `Budi Kurniawan` ditemukan (kolom Division, substring, tidak membedakan huruf besar kecil)
7. Ganti isi kotak search dengan `ft-02`, tekan Enter
8. Verifikasi baris `Budi Kurniawan` ditemukan (kolom Employee ID, substring, tidak membedakan huruf besar kecil)
9. Ganti isi kotak search dengan `fauz`, tekan Enter
10. Verifikasi baris `Budi Kurniawan` ditemukan (kolom Represented By, substring, tidak membedakan huruf besar kecil)

### TC-GS-NLU-258: Empty state saat Search tidak ditemukan

11. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
12. Verifikasi empty state: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`

### TC-GS-NLU-260: Search memangkas spasi tepi query dan memperlakukan karakter khusus sebagai teks

13. Ketik Search `  Rina  ` (dua spasi di tepi), tekan Enter
14. Verifikasi hasil sama dengan Search `Rina`: baris `Rina Marlina` tampil
15. Verifikasi isi kotak Search tidak berubah (tetap `  Rina  `)
16. Ganti isi kotak search dengan `<script>alert(1)</script>`, tekan Enter
17. Verifikasi tidak ada hasil pencarian (empty state `No results found` tampil)
18. Verifikasi tidak ada skrip dijalankan (tidak ada dialog `alert` browser; teks dicocokkan sebagai teks biasa)

### TC-GS-NLU-261: Kolom tanggal Last Update tidak dapat dicari lewat Search

19. Ganti isi kotak search dengan `Budi Kurniawan`, tekan Enter
20. Catat nilai sel Last Update baris `Budi Kurniawan` sebagaimana tampil
21. Ganti isi kotak search dengan nilai Last Update yang dicatat, tekan Enter
22. Verifikasi tabel menampilkan `No results found` (penyaringan tanggal hanya lewat Filter Panel)
23. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): langkah mencari `Budi Kurniawan` dan mencatat Last Update pada TC-GS-NLU-261 (Search untuk menemukan baris target, R-16), dan langkah terakhir (klik `(←)`) yang mengosongkan Search.
- Asersi tambahan (S-03): pada TC-GS-NLU-260 baris pembanding `Rina Marlina` dipakai sebagai anchor positif untuk asersi absence (bagian 8b butir 2); empty state `No results found` pada TC-GS-NLU-260 menjadi anchor untuk asersi "tidak ada skrip dijalankan".
- Pembagian TC lintas spec: TC-GS-NLU-259 (siklus interaksi Search) ada di spec 133.
- Mode FE+BE: hasil Search dibaca dari backend nyata; tidak ada intercept.
- Temuan untuk QA:
  - TC-GS-NLU-260 Expected b ("tidak ada skrip dijalankan") tidak menyebut cara pengamatannya; spec memakai pengamatan ada tidaknya dialog `alert` browser.
  - TC-GS-NLU-261 precondition d menyebut tanggal Last Update `Budi Kurniawan` "diketahui" tanpa menyebut sumbernya; spec membacanya dari sel tabel.
  - Posisi baris pada halaman 1 bergantung pada urutan default Name A-Z dan populasi Pre-setup; asersi memakai baris pembanding yang termuat oleh Search.
