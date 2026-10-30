---
id: TC-GS-GSET-E2E-051-defense-in-depth-bypass-client-error-inline-currency-dan-time-zone
title: "Bypass DOM A"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-164
  - TC-GS-GSET-165
  - TC-GS-GSET-166
  - TC-GS-GSET-167
coverage:
  web: automated
---

# Bypass DOM A

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > General Settings.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` dan pemulihan record ke baseline Pre-setup No 10): lihat `suite.md`, bagian Hook suite; spec ini tidak mengatur flag sendiri.
- Data: record General Settings Client A pada baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`); label Currency Code `IDR` = `Rp - Indonesian Rupiah`, label Time Zone `Asia/Jakarta` = `(UTC+07:00) Bangkok, Hanoi, Jakarta` (PRD §4.3a). Spec tidak membuat data dinamis dan tidak mengubah state (semua Save ditolak server). "Kosong" berarti nilai string kosong `""`.
- Kemampuan teknis: (a) menyetel nilai elemen Select langsung lewat DOM, melewati pilihan dropdown dan validasi klien (injeksi nilai); (b) menangani dialog `beforeunload` browser pada muat ulang halaman (F5) saat form belum disimpan (dialog diterima, S-08).
- Tabel "Currency Code" (dipakai langkah 2 sampai 10):

  | Urutan | TC | Nilai yang diinjeksi | Pesan error inline |
  |---|---|---|---|
  | 1 | TC-GS-GSET-164 | `""` (kosong) | `Currency Code must not be empty` |
  | 2 | TC-GS-GSET-165 | `ZZZ` (di luar enum) | `Invalid currency code` |

- Tabel "Time Zone" (dipakai langkah 12 sampai 19):

  | Urutan | TC | Nilai yang diinjeksi | Pesan error inline |
  |---|---|---|---|
  | 1 | TC-GS-GSET-166 | `""` (kosong) | `Time Zone must not be empty` |
  | 2 | TC-GS-GSET-167 | `Mars/Olympus` (bukan IANA kurasi) | `Invalid time zone` |

- Tidak ada state global yang diubah. Suite berjalan serial (`parallel: false`).
- Layar awal Global Settings > General Settings dibuka di hook `beforeEach` (konvensi bagian 4); tiap iterasi berakhir dengan muat ulang halaman sehingga iterasi berikutnya mulai dari halaman bersih.

## Test Steps

### TC-GS-GSET-164 dan TC-GS-GSET-165: Bypass client pada Select Currency Code

1. Untuk setiap baris tabel "Currency Code" (urutan 1 sampai 2), lakukan langkah 2 sampai 10 dengan nilai baris itu
2. Injeksi nilai kolom Nilai yang diinjeksi ke Select Currency Code lewat DOM
3. Klik `[Save]`
4. Klik `[Change Currency]` pada dialog Change Currency
5. Verifikasi error inline di bawah field Currency Code sesuai kolom Pesan error inline
6. Verifikasi field Currency Code bergaya error
7. Verifikasi tidak ada toast sukses
8. Verifikasi form tetap unsaved (tombol `[Save]` tetap aktif)
9. Muat ulang halaman (F5) dan terima dialog `beforeunload`
10. Verifikasi Select Currency Code menampilkan nilai tersimpan `Rp - Indonesian Rupiah` (tidak berubah)

### TC-GS-GSET-166 dan TC-GS-GSET-167: Bypass client pada Select Time Zone

11. Untuk setiap baris tabel "Time Zone" (urutan 1 sampai 2), lakukan langkah 12 sampai 19 dengan nilai baris itu
12. Injeksi nilai kolom Nilai yang diinjeksi ke Select Time Zone lewat DOM
13. Klik `[Save]`
14. Verifikasi error inline di bawah field Time Zone sesuai kolom Pesan error inline
15. Verifikasi field Time Zone bergaya error
16. Verifikasi tidak ada toast sukses
17. Verifikasi form tetap unsaved (tombol `[Save]` tetap aktif)
18. Muat ulang halaman (F5) dan terima dialog `beforeunload`
19. Verifikasi Select Time Zone menampilkan nilai tersimpan `(UTC+07:00) Bangkok, Hanoi, Jakarta` (tidak berubah)

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (TC-GS-GSET-164 sampai TC-GS-GSET-167). Mode: FE+BE. Kelas: defense-in-depth (bypass validasi klien, prinsip 13 butir a).
- Ukuran: langkah berulang (bagian 8b butir 7). Blok Currency Code (langkah 2 sampai 10) diulang dua kali dan blok Time Zone (langkah 12 sampai 19) diulang dua kali; ekspansi 1 + 9 x 2 + 1 + 8 x 2 = 36 langkah, sedikit di atas batas sekitar 35. Alasan pertahanan: seluruh blok satu kelas, berdiri sendiri (kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna), dan tiap iterasi mulai dari halaman bersih.
- Dipisah dari spec 052 karena gabungan langkahnya jauh melewati batas ukuran (36 + 49 = 85 langkah dengan ekspansi, batas sekitar 35).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 3, 4, 9, 11, 12, 13, dan 18 (injeksi, Save, konfirmasi dialog Change Currency, dan muat ulang). Dialog Change Currency muncul pada TC-GS-GSET-164 dan TC-GS-GSET-165 karena nilai Currency Code yang diinjeksi berbeda dari nilai tersimpan (`GSET-LOGIC-04a`); langkah 4 mengonfirmasinya sebelum request simpan terkirim.
- Muat ulang (F5) pada form yang belum disimpan memunculkan dialog `beforeunload` browser; kemampuan menanganinya ditulis di Prerequisites (S-08). Muat ulang juga memulihkan form sehingga iterasi berikutnya mulai dari halaman bersih (S-09).
- "Form tetap unsaved" ditafsirkan sebagai tombol `[Save]` masih aktif (nilai belum di-rebase ke nilai tersimpan, `S-07` PRD menyebut tombol disabled hanya setelah Save berhasil).
- Asersi "tidak ada toast sukses" diletakkan sesudah `Verifikasi` error inline, yang menjadi anchor bahwa respons server sudah diproses (bagian 8b butir 2).
- Dependensi TC-GS-GSET-164 sampai TC-GS-GSET-167 adalah "-" pada TC.
- Temuan untuk QA:
  - TC-GS-GSET-164 dan TC-GS-GSET-165 menyertakan langkah `[Change Currency]` sedangkan TC-GS-GSET-166 dan TC-GS-GSET-167 tidak, konsisten dengan `GSET-LOGIC-04a` (dialog hanya untuk perubahan Currency Code).
  - TC-GS-GSET-164 sampai TC-GS-GSET-167 menyebut "form tetap unsaved" tanpa elemen yang diamati; spec mengasersi tombol `[Save]` tetap aktif.
  - Cara injeksi nilai ke komponen Select (nilai `""` atau di luar opsi) bergantung pada implementasi komponen; kemampuan itu disediakan tim FE.
