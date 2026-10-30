---
id: TC-GS-GSET-E2E-052-defense-in-depth-bypass-client-error-inline-date-time-format-dan-session-idle
title: "Bypass DOM B"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-168
  - TC-GS-GSET-169
  - TC-GS-GSET-170
  - TC-GS-GSET-171
  - TC-GS-GSET-172
  - TC-GS-GSET-173
coverage:
  web: automated
---

# Bypass DOM B

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > General Settings.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` dan pemulihan record ke baseline Pre-setup No 10): lihat `suite.md`, bagian Hook suite; spec ini tidak mengatur flag sendiri.
- Data: record General Settings Client A pada baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`). Spec tidak membuat data dinamis dan tidak mengubah state (semua Save ditolak server). "Kosong" berarti nilai string kosong `""`.
- Kemampuan teknis: (a) menyetel nilai elemen Select langsung lewat DOM, melewati pilihan dropdown dan validasi klien (injeksi nilai); (b) menangani dialog `beforeunload` browser pada muat ulang halaman (F5) saat form belum disimpan (dialog diterima, S-08).
- Tabel "Bypass Select" (dipakai langkah 2 sampai 9):

  | Urutan | TC | Field | Nilai yang diinjeksi | Pesan error inline | Nilai tersimpan |
  |---|---|---|---|---|---|
  | 1 | TC-GS-GSET-168 | `Date Format` | `""` (kosong) | `Date Format must not be empty` | `dd/MM/yy` |
  | 2 | TC-GS-GSET-169 | `Date Format` | `YYYY-MM-DD` (di luar enum) | `Invalid date format` | `dd/MM/yy` |
  | 3 | TC-GS-GSET-170 | `Time Format` | `""` (kosong) | `Time Format must not be empty` | `HH:mm` |
  | 4 | TC-GS-GSET-171 | `Time Format` | `h:mm a` (di luar enum) | `Invalid time format` | `HH:mm` |
  | 5 | TC-GS-GSET-172 | `Session Idle Timeout` | `""` (kosong) | `Session Idle Timeout must not be empty` | `30 minutes` |
  | 6 | TC-GS-GSET-173 | `Session Idle Timeout` | `45` (di luar enum) | `Invalid session idle timeout value` | `30 minutes` |

- Tidak ada state global yang diubah. Suite berjalan serial (`parallel: false`).
- Layar awal Global Settings > General Settings dibuka di hook `beforeEach` (konvensi bagian 4); tiap iterasi berakhir dengan muat ulang halaman sehingga iterasi berikutnya mulai dari halaman bersih.

## Test Steps

### TC-GS-GSET-168 sampai TC-GS-GSET-173: Bypass client pada Select Date Format, Time Format, dan Session Idle Timeout

1. Untuk setiap baris tabel "Bypass Select" (urutan 1 sampai 6), lakukan langkah 2 sampai 9 dengan nilai baris itu
2. Injeksi nilai kolom Nilai yang diinjeksi ke Select kolom Field lewat DOM
3. Klik `[Save]`
4. Verifikasi error inline di bawah field kolom Field sesuai kolom Pesan error inline
5. Verifikasi field kolom Field bergaya error
6. Verifikasi tidak ada toast sukses
7. Verifikasi form tetap unsaved (tombol `[Save]` tetap aktif)
8. Muat ulang halaman (F5) dan terima dialog `beforeunload`
9. Verifikasi Select kolom Field menampilkan nilai tersimpan sesuai kolom Nilai tersimpan (tidak berubah)

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (TC-GS-GSET-168 sampai TC-GS-GSET-173). Mode: FE+BE. Kelas: defense-in-depth (bypass validasi klien, prinsip 13 butir a).
- Ukuran: langkah 2 sampai 9 diulang enam kali (bagian 8b butir 7); ekspansi 1 + 8 x 6 = 49 langkah, di atas batas sekitar 35. Alasan pertahanan: seluruh iterasi satu kelas dan satu prosedur identik (parameter di tabel Prerequisites, tanpa langkah bersyarat), berdiri sendiri (kegagalan satu field tidak membuat field lain kehilangan makna), dan tiap iterasi mulai dari halaman bersih. Memisahkan per field hanya menggandakan login, hook, dan baseline tanpa alur baru.
- Dipisah dari spec 051 karena gabungan langkahnya jauh melewati batas ukuran (49 + 36 = 85 langkah dengan ekspansi, batas sekitar 35).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 3, dan 8 (injeksi, Save, dan muat ulang). Tidak ada dialog Change Currency karena Currency Code tidak diubah.
- Muat ulang (F5) pada form yang belum disimpan memunculkan dialog `beforeunload` browser; kemampuan menanganinya ditulis di Prerequisites (S-08). Muat ulang juga memulihkan form sehingga iterasi berikutnya mulai dari halaman bersih (S-09).
- "Form tetap unsaved" ditafsirkan sebagai tombol `[Save]` masih aktif (nilai belum di-rebase ke nilai tersimpan).
- Asersi "tidak ada toast sukses" diletakkan sesudah `Verifikasi` error inline, yang menjadi anchor bahwa respons server sudah diproses (bagian 8b butir 2).
- Dependensi TC-GS-GSET-168 sampai TC-GS-GSET-173 adalah "-" pada TC.
- Temuan untuk QA:
  - TC-GS-GSET-168 sampai TC-GS-GSET-173 menyebut "form tetap unsaved" tanpa elemen yang diamati; spec mengasersi tombol `[Save]` tetap aktif.
  - Nilai tersimpan Date Format pada TC ditulis sebagai kode format (`dd/MM/yy`); label opsi di dropdown (mis. disertai contoh tanggal, TC-GS-GSET-08) tidak disebut pada Expected, sehingga `Verifikasi` langkah 9 memakai kode format dan teks lengkap label opsi mengikuti tampilan aplikasi.
  - Cara injeksi nilai ke komponen Select (nilai `""` atau di luar opsi) bergantung pada implementasi komponen; kemampuan itu disediakan tim FE.
