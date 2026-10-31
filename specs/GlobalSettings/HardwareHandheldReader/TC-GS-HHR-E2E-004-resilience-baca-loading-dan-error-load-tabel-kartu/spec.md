---
id: TC-GS-HHR-E2E-004-resilience-baca-loading-dan-error-load-tabel-kartu
title: "Resilience Baca Halaman Handheld Reader: State Loading, Error Load Tabel, dan Error Load License Counter Cards dengan Try Again"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-HHR-20
  - TC-GS-HHR-21
  - TC-GS-HHR-22
coverage:
  web: automated
---

# Resilience Baca Halaman Handheld Reader: State Loading, Error Load Tabel, dan Error Load License Counter Cards dengan Try Again

## Prerequisites

- Mode: mock (seluruh API di-mock; dijalankan tim FE sebagai integration test tanpa backend nyata, konvensi bagian 2 dan bagian 6 "Resilience `Mode: mock`"). Asersi hanya perilaku FE atas respons mock (state Loading, Error State, tombol `[Try Again]`, isi tabel dan kartu hasil baca ulang respons mock); tidak ada asersi state server nyata.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1, Client A, plan Growth). Identitas pengguna, capability, dan menu sidebar disediakan tim FE sebagai respons mock (API pendukung di luar sumber modul); tidak ada login ke backend nyata dan tidak ada password.
- Layar awal: halaman Global Settings > Hardware > Handheld Reader dibuka di `## Test Steps` karena pembukaan halaman dengan respons mock yang berbeda adalah aksi yang diuji pada tiap TC.
- Guided Tooltip: flag halaman Handheld Reader (`guided_tooltip_seen_gs-handheld-reader`) bernilai seen (true) di respons mock flag, disediakan tim FE (API pendukung di luar sumber modul), supaya walkthrough tidak muncul menutupi tabel dan kartu.
- Kebutuhan mock: endpoint yang dipanggil halaman pada kondisi tes diambil dari kontrak API modul (`global-settings/hardware-handheld-reader/API/openapi.yaml`) dan respons yang dipaksa per TC:

| Request | Endpoint (openapi.yaml) | Kondisi normal (default) | TC-GS-HHR-20 | TC-GS-HHR-21 | TC-GS-HHR-22 |
|---|---|---|---|---|---|
| Daftar reader | `POST /v2/hardware-tagging/handheld-readers/list` | 200, berisi Seed Reader A (DD-01 s.d. DD-10, 10 reader) | respons ditunda | 500 | 200 normal |
| Kuota License Counter Cards | `GET /v2/enterprise-management/handheld-readers/quotas` | 200, `Short Range` 5 dari 8, `Long Range` 5 dari 6 | respons ditunda | 200 normal | 500 |
| Opsi Filter | `POST /v2/hardware-tagging/handheld-readers/options` | 200 normal | 200 normal | 200 normal | 200 normal |

- Request opsi Filter tidak dipakai langkah spec ini (panel Filter tidak dibuka); mock membalasnya 200 normal bila halaman memanggilnya saat dimuat. API pendukung di luar sumber modul (identitas pengguna, menu sidebar, flag Guided Tooltip) disediakan tim FE sebagai respons mock.
- Seed Reader A (Tabel Data Uji Dinamis TC DD-01 s.d. DD-10) dipakai sebagai isi respons mock daftar reader; tidak ada Data Dinamis lain.
- Kemampuan teknis: mock respons per request (200, 500, tunda hingga dilepas) dan pelepasan mock dalam satu sesi tanpa memuat ulang halaman; pembacaan state komponen Loading dan Error State.
- State global: tidak ada. Mock dilepas segera setelah pemicu selesai pada tiap TC; hook `after` melepas semua mock sebagai cadangan.

## Test Steps

### TC-GS-HHR-20: State loading tabel dan License Counter Cards saat data dimuat

1. Pasang mock penundaan respons pada request daftar reader dan request kuota
2. Buka Global Settings > Hardware > Handheld Reader
3. Verifikasi tabel menampilkan varian DataTable Loading selama request tertunda
4. Verifikasi License Counter Cards menampilkan state Loading selama request tertunda
5. Lepaskan penundaan sehingga respons normal diterima
6. Verifikasi tabel menampilkan data 10 baris
7. Verifikasi License Counter Cards menampilkan nilai kartu `Short Range` `5 of 8` dan `Long Range` `5 of 6`

### TC-GS-HHR-21: Error load tabel menampilkan Try Again dan bukan empty state

8. Pasang mock request daftar reader membalas 500
9. Buka Global Settings > Hardware > Handheld Reader lewat address bar
10. Verifikasi tabel menampilkan varian Error State dengan teks `Unable to load this data.`
11. Verifikasi tombol `[Try Again]` tampil pada Error State tabel
12. Verifikasi area tabel tidak menampilkan empty state `No handheld reader yet`
13. Lepas mock 500 sehingga request daftar reader kembali membalas 200 dengan Seed Reader A
14. Klik `[Try Again]`
15. Verifikasi tabel menampilkan data 10 baris

### TC-GS-HHR-22: Error load License Counter Cards menampilkan opsi muat ulang

16. Pasang mock request kuota membalas 500
17. Buka Global Settings > Hardware > Handheld Reader lewat address bar
18. Verifikasi License Counter Cards menampilkan state Error load dengan teks `Unable to load this data.`
19. Verifikasi tombol `[Try Again]` tampil pada kartu
20. Lepas mock 500 sehingga request kuota kembali membalas 200
21. Klik `[Try Again]` pada kartu
22. Verifikasi kartu `Short Range` menampilkan `5 of 8`
23. Verifikasi kartu `Long Range` menampilkan `5 of 6`

## Notes

- Mode: mock. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 20, 21, 22 (urutan TC sumber); tiap TC memulai dari pembukaan halaman dengan kondisi mock sendiri sehingga tidak saling bergantung.
- Spec ini kelas b (fault injection / resilience) dengan `Mode: mock` karena seluruh asersi adalah perilaku FE atas respons mock (konvensi bagian 6 "Resilience `Mode: mock`" `[KEPUTUSAN 2026-10-29]`). Asersi isi tabel dan nilai kartu pada langkah 6, 7, 15, 22, dan 23 adalah baca ulang respons mock yang diminta Expected TC (TC-GS-HHR-20 c, 21 b, 22 b).
- TC-GS-HHR-20, 21, dan 22 tidak memuat asersi state server nyata; TC FE+BE untuk kegagalan tulis ada di spec lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5, 13, dan 20 (melepas mock segera sesudah pemicu selesai, ditulis sebagai "Hapus intercept" di TC), langkah 9 dan 17 (membuka ulang halaman lewat address bar karena halaman sudah terbuka dari TC sebelumnya dan pembukaan dengan mock berbeda adalah pemicu).
- Langkah 12 (absence empty state `No handheld reader yet`) didahului langkah 10 dan 11 (Error State dan `[Try Again]` tampil di area tabel yang sama) sebagai anchor positif.
- Temuan untuk QA:
  - TC-GS-HHR-22 langkah 4 menyebut "klik `[Try Again]` pada kartu" tanpa menyebut apakah tiap kartu punya tombol sendiri atau satu tombol untuk kedua kartu; spec mengasersi satu tombol `[Try Again]` pada kartu dan mengklik tombol itu.
  - TC-GS-HHR-20 Expected c ("data 10 baris dan nilai kartu tampil") tidak menyebut nilai kartu; spec memakai nilai Seed Reader A (`5 of 8` dan `5 of 6`, sesuai TC-GS-HHR-15).
  - TC-GS-HHR-21 dan 22 menyebut "Hapus intercept" pada backend nyata; pada `Mode: mock` setara dengan mengganti mock ke respons 200 normal.
