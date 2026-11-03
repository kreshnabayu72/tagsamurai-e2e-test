---
id: TC-AC-DN-E2E-038-resilience-delete-gagal
title: "Resilience: Delete Single Gagal, Retry, dan Tanpa Respons"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-196
  - TC-AC-DN-198
  - TC-AC-DN-197
coverage:
  web: automated
---

# Resilience: Delete Single Gagal, Retry, dan Tanpa Respons

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Login di hook `before` spec ini sebagai Total Control (Principal, Default User) (Pre-setup #1); halaman dibuka hook `beforeEach` suite. Jaring pengaman S-09 hook `beforeEach` dan penyetelan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.AC_TC_PASSWORD`).
- Suite berjalan serial (`parallel: false`).
- Akun yang dipakai (email dirujuk lewat `Fixture.settings-device-name.<kunci>`; fixture belum ada, disediakan tim FE):

| Pre-setup | Role | Nama user | Email | Kunci fixture | Env var password | Dipakai di TC |
|---|---|---|---|---|---|---|
| #1 | Total Control (Principal, Default User) | Budi Santoso | `totalControlDevName_automated_{namaCompany}@qwertysystem.net` | `akunTotalControl` | `Spectra.env.AC_TC_PASSWORD` | TC-AC-DN-196, 198, 197 |

- Env var password: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data milik spec (S-06, S-12): `Cable Tester {runId}-038` (Category `Accessory`, Measurement `Unit`, tanpa SKU dan tanpa unit BYO) dibuat fixture backend di hook `before` (disediakan tim FE/BE); terhapus oleh langkah retry TC-AC-DN-197, hook `after` menghapus sisanya bila ada. Device Name inti (#16) tidak dipakai sebagai target hapus.
- Kemampuan teknis (disediakan tim FE/BE): `Spectra.intercept()` untuk menjawab request dengan status 500, menahan respons sampai batas waktu, dan menunda respons; intercept dilepas segera setelah pemicunya selesai (S-09). Jeda nyata 10 detik pada langkah "Tunggu 10 detik" dipilih spec untuk mengamati toast yang tidak hilang sendiri (di bawah batas ±30 detik, bagian 6).

## Test Steps

1. Ketik Search `Cable Tester {runId}-038`, tekan Enter
2. Klik ikon aksi pada kolom Actions baris `Cable Tester {runId}-038` lalu klik `Delete`

### TC-AC-DN-196: Delete gagal karena error server menampilkan toast error dan dialog tetap terbuka

3. Paksa respons server 500 pada request hapus dengan intercept jaringan
4. Klik `[Delete]`
5. Verifikasi toast error: "Error, failed to delete device name."
6. Tunggu 10 detik tanpa menutup toast
7. Verifikasi toast tidak hilang otomatis sampai di-dismiss
8. Verifikasi dialog konfirmasi tetap terbuka dengan bullet `Cable Tester {runId}-038`
9. Verifikasi tombol `[Delete]` dan `[Cancel]` kembali aktif
10. Verifikasi baris `Cable Tester {runId}-038` tetap ada pada List
11. Lepas intercept jaringan
12. Tutup toast error

### TC-AC-DN-198: Delete yang tidak mendapat respons menampilkan toast koneksi dan dialog tetap terbuka

13. Tunda respons request hapus melewati batas timeout dengan intercept jaringan
14. Klik `[Delete]`
15. Verifikasi toast error: "Connection problem. Please try again." tanpa tombol aksi
16. Verifikasi dialog konfirmasi tetap terbuka dan tombol `[Delete]` kembali aktif untuk coba ulang
17. Verifikasi baris `Cable Tester {runId}-038` tetap ada pada List
18. Lepas intercept jaringan
19. Tutup toast error

### TC-AC-DN-197: Retry Delete setelah error server berhasil dari dialog yang sama

20. Paksa respons server 500 pada request hapus dengan intercept jaringan
21. Klik `[Delete]`
22. Hapus intercept lalu tutup toast error
23. Klik `[Delete]` lagi
24. Verifikasi toast sukses: "Success, device name has been deleted."
25. Verifikasi dialog tertutup
26. Verifikasi baris `Cable Tester {runId}-038` tidak lagi ada pada List
27. Klik `(←)` pada kotak Search

## Notes

- Spec resilience (kelas b): kegagalan server, tanpa respons, dan retry pada Delete single yang dipaksa lewat intercept di atas backend nyata (bagian 6, `FE+BE`). Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan (S-10): TC sumber diurutkan 196, 198, 197 (bukan 196, 197, 198) agar aksi yang menghapus data berada di akhir dan dialog Delete yang sama dipakai berulang tanpa dibuka ulang (langkah 1 sampai 2 mencakup langkah 1 sampai 3 tiap TC).
- Penyimpangan data (S-06): target hapus `Cable Tester` (Pre-setup #16) diganti record milik spec bersuffix.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16) dan mengosongkannya lewat `(←)`; melepas intercept dan menutup toast error sebelum diasersi lagi (R-12).
- Temuan untuk QA:
  - Post Condition TC-AC-DN-196 ("tidak ada entri log") dan TC-AC-DN-197 ("satu set entri Delete tercatat") tidak punya langkah observasi dan tidak diasersi (S-01, S-05).
