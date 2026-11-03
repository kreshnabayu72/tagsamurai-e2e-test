---
id: TC-AC-DN-E2E-034-defense-validasi-dan-guard-server
title: "Defense-in-Depth: Server Menolak Emoji, Duplikat, dan Delete/Edit yang Melanggar Guard"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-565
  - TC-AC-DN-566
  - TC-AC-DN-567
  - TC-AC-DN-568
  - TC-AC-DN-569
  - TC-AC-DN-570
coverage:
  web: automated
---

# Defense-in-Depth: Server Menolak Emoji, Duplikat, dan Delete/Edit yang Melanggar Guard

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal, Default User) (Pre-setup #1); halaman dibuka hook `beforeEach` suite. Jaring pengaman S-09 hook `beforeEach` dan penyetelan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.AC_TC_PASSWORD`).
- Suite berjalan serial (`parallel: false`).
- Akun yang dipakai (email dirujuk lewat `Fixture.settings-device-name.<kunci>`; fixture belum ada, disediakan tim FE):

| Pre-setup | Role | Nama user | Email | Kunci fixture | Env var password | Dipakai di TC |
|---|---|---|---|---|---|---|
| #1 | Total Control (Principal, Default User) | Budi Santoso | `totalControlDevName_automated_{namaCompany}@qwertysystem.net` | `akunTotalControl` | `Spectra.env.AC_TC_PASSWORD` | TC-AC-DN-565 sampai TC-AC-DN-570 |

- Env var password: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP untuk request langsung ke server dengan login API (password) tiap akun; token tidak dihitung sebagai sesi web (`suite.md`). Request langsung hanya mengasersi respons server (status); state data diamati lewat List pada sesi Total Control UI (hook `before`) dan fixture backend (bagian 8b butir 1).
- Penghapusan record milik spec dan pemulihan dilakukan fixture backend di hook `after`.
- Data Pre-setup: Measurement `Unit` (#13) dan Pohon Uji Kategori (#14) dibaca saja; seed SKU dan unit BYO (#22) dibuat tim FE/BE.
- Data milik spec (S-06, S-12), dibuat fixture backend di hook `before`: `Cable Tester {runId}-034` (Category `Accessory`, Measurement `Unit`); `RFID Reader {runId}-034` (Category `UHF Handheld`, Measurement `Unit`, tiga SKU Brand A/Model R1, Brand B/Model R2, Brand C/Model R3); `Field Radio {runId}-034` (Category `Accessory`, Measurement `Box`, tanpa SKU, unit BYO Hardware aktif di Company E); `Gate Antenna {runId}-034` (Category `Antenna`, Measurement `Unit`, SKU Brand A/Model G1 dan Brand B/Model G2). Request Create yang diterima server membuat `Reader Umum {runId}-034`; hook `after` menghapus semua record milik spec bersama SKU dan unit BYO-nya.
- Kemampuan membaca jumlah entri Changelog (total dan per Device Name) sebelum aksi disediakan tim FE/BE (bagian 8b butir 10); asersi Changelog memakai selisih terhadap baseline (S-12).

## Test Steps

### TC-AC-DN-565: Server menolak nama Device Name berisi karakter emoji pada request Create

1. Kirim request Create Device Name `Antena Gudang {runId}-034` diikuti karakter emoji U+1F60A (Measurement `Unit`, Category `Antenna`) memakai klien HTTP dengan sesi Total Control
2. Verifikasi server menolak request dengan kesalahan validasi pada field Device Name (422 Validation, error-handling-convention.md §2)
3. Buka halaman `Settings > Device > Device Name` dan ketik Search `Antena Gudang {runId}-034`, tekan Enter
4. Verifikasi hasil Search menampilkan empty state "No results found" sehingga tidak ada Device Name berawalan `Antena Gudang {runId}-034` tersimpan
5. Klik `(←)` pada kotak Search

### TC-AC-DN-566: Server menolak Device Name duplikat berbeda huruf besar-kecil pada request Create

6. Kirim request Create Device Name `cable tester {runId}-034` (Measurement `Unit`, Category `Accessory`) memakai klien HTTP dengan sesi Total Control
7. Verifikasi server menolak request karena nama sudah ada
8. Ketik Search `cable tester {runId}-034`, tekan Enter
9. Verifikasi List memuat tepat satu baris `Cable Tester {runId}-034`
10. Klik `(←)` pada kotak Search

### TC-AC-DN-567: Server menerima Category yang punya anak pada request Create

11. Kirim request Create Device Name `Reader Umum {runId}-034` (Measurement `Unit`, Category `Handheld Reader`) memakai klien HTTP dengan sesi Total Control
12. Verifikasi server menerima request
13. Verifikasi lewat fixture backend Device Name `Reader Umum {runId}-034` tersimpan dengan Category `Handheld Reader`
14. Ketik Search `Reader Umum {runId}-034`, tekan Enter
15. Verifikasi pencarian menampilkan baris `Reader Umum {runId}-034`
16. Verifikasi baris `Reader Umum {runId}-034` menampilkan Category badge `Handheld Reader`
17. Klik `(←)` pada kotak Search

### TC-AC-DN-568: Server menolak Delete Device Name ber-SKU pada request langsung

18. Kirim request Delete Device Name `RFID Reader {runId}-034` memakai klien HTTP dengan sesi Total Control
19. Verifikasi server menolak penghapusan karena Device Name masih dipakai
20. Ketik Search `RFID Reader {runId}-034`, tekan Enter
21. Verifikasi baris `RFID Reader {runId}-034` tetap ada dengan Brand "Brand A", "Brand B", dan "Brand C"
22. Klik `(←)` pada kotak Search

### TC-AC-DN-569: Server menolak Delete Device Name ber-unit BYO pada request langsung

23. Kirim request Delete Device Name `Field Radio {runId}-034` memakai klien HTTP dengan sesi Total Control
24. Verifikasi server menolak penghapusan karena Device Name masih dipakai unit terdaftar
25. Ketik Search `Field Radio {runId}-034`, tekan Enter
26. Verifikasi baris `Field Radio {runId}-034` tetap ada di List
27. Klik `(←)` pada kotak Search

### TC-AC-DN-570: Server menolak perubahan Category Device Name ber-SKU pada request Edit langsung

28. Catat baseline jumlah total entri Changelog dan jumlah entri Changelog untuk `Gate Antenna {runId}-034` sebelum request
29. Kirim request Edit Device Name `Gate Antenna {runId}-034` dengan Category `UHF Handheld` memakai klien HTTP dengan sesi Total Control
30. Verifikasi server menolak request dengan kesalahan validasi pada field Category dengan pesan "This device name already has SKUs. Category cannot be changed."
31. Ketik Search `Gate Antenna {runId}-034`, tekan Enter
32. Verifikasi baris `Gate Antenna {runId}-034` tetap menampilkan badge Category "Antenna"
33. Klik ikon Changelog
34. Verifikasi jumlah total entri modal Changelog sama dengan baseline
35. Verifikasi tidak ada entri baru untuk `Gate Antenna {runId}-034` dibanding baseline
36. Tutup modal "Changelog: Device Name"
37. Klik `(←)` pada kotak Search

## Notes

- Spec defense-in-depth (kelas a): validasi dan guard sisi server lewat request langsung. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC-AC-DN-565, 566, 567, 568, 569, dan 570 adalah TC defense-in-depth (kelas a) dengan Expected respons API; tetap FE+BE walau tumpang tindih dengan `tc-settings-device-name-backend.md`, karena TC granular tetap sumber dan tiap TC tepat satu spec.
- Penyimpangan data (S-06, S-12): record `Cable Tester`, `RFID Reader`, `Field Radio`, `Gate Antenna` (Pre-setup #16 di TC) diganti record bersuffix milik spec dengan struktur SKU dan unit BYO yang sama; nama request memakai suffix yang sama.
- Langkah penghubung (S-03): Search untuk memeriksa hasil pada List (R-16), mengosongkan Search lewat `(←)`, menutup modal Changelog, mencatat baseline Changelog.
- Ukuran spec (37 langkah, di atas 35 langkah; alasan R3): seluruh blok satu kelas harness (a), satu akun, klien HTTP yang sama, dan dataset milik spec yang sama; tiap blok berdiri sendiri.
- Temuan untuk QA:
  - TC-AC-DN-570 Expected c menyebut "11 entri" sebagai angka absolut; karena Changelog adalah audit trail yang tumbuh (S-12), spec memakai selisih terhadap baseline.
  - TC-AC-DN-567 (Category yang punya anak diterima server) bertumpuan pada keputusan NC-19 dan berbeda dengan form UI yang hanya menawarkan leaf sebagai pilihan.
  - TC-AC-DN-566 tidak menyebut Category; spec memakai `Accessory` seperti baris asalnya.
