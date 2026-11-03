---
id: TC-GS-NLU-E2E-138-resilience-aksi-kegagalan-server-saat-download
title: "Resilience aksi: kegagalan server saat Download list, Changelog, Borrowed Assets, Assigned Assets"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-298
  - TC-GS-NLU-498
coverage:
  web: automated
---

# Resilience aksi: kegagalan server saat Download list, Changelog, Borrowed Assets, Assigned Assets

## Prerequisites

- Mode: FE+BE. Spec memaksa respons 500 pada request Download lewat `Spectra.intercept()` di atas backend nyata.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 500 pada request yang disebut tiap langkah, parsial di atas backend nyata (bagian 6); nama endpoint ditentukan tim FE pada tahap script (S-13). Hook `after` melepas semua intercept walau spec gagal di tengah.
- Data Pre-setup (hanya dibaca, tidak diubah atau dihapus; Tabel Data Uji Pre-setup No. 11 dan 14): Non-Login User `Budi Kurniawan` dengan transaksi Borrowed `BRW-20260610-0001` (Laptop - 1) dan Assigned `ASG-20260505-0001` (Company Vehicle B1234XY). Spec ini tidak menulis ke record itu karena setiap Download digagalkan lewat intercept.
- Request yang dipaksa 500: Download list Non-Login User (TC-GS-NLU-298) serta Download Modal Changelog agregat, Tab Changelog Detail, Borrowed Assets, dan Assigned Assets (TC-GS-NLU-498), satu per satu dan dilepas sesudah tiap blok.
- Data milik spec: tidak ada. Nama berkas pada toast mengikuti Expected TC (`Budi-Kurniawan`) karena Detail yang dibuka adalah record Pre-setup `Budi Kurniawan` (S-06, S-02).
- Pemulihan: hook `after` melepas intercept.
- Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.

## Test Steps

### TC-GS-NLU-298: Kegagalan server saat Download menampilkan toast error

1. Pasang intercept yang memaksa respons 500 untuk request Download list Non-Login User
2. Klik Download > `Download as CSV`
3. Verifikasi Toast error `Error, failed to download Non-Login-Users.`
4. Verifikasi tidak ada berkas terunduh
5. Lepas intercept (pulihkan response)

### TC-GS-NLU-498: Kegagalan server saat Download Changelog agregat, Tab Changelog Detail, Borrowed Assets, dan Assigned Assets

6. Pasang intercept yang memaksa respons 500 untuk request Download Changelog agregat
7. Klik icon `Changelog` pada Table Tools, lalu klik Download > `Download as CSV`
8. Verifikasi Toast error `Error, failed to download Changelog-Non-Login-User.`
9. Verifikasi tidak ada berkas terunduh pada Modal Changelog agregat
10. Lepas intercept (pulihkan response), lalu tutup Modal Changelog dengan `✕`
11. Ketik Search `Budi Kurniawan`, tekan Enter, klik Name baris `Budi Kurniawan` (tanpa suffix `{runId}`) untuk membuka Detail
12. Pasang intercept yang memaksa respons 500 untuk request Download Changelog Detail
13. Klik tab `Changelog`, lalu klik Download > `Download as CSV`
14. Verifikasi Toast error `Error, failed to download Changelog-Non-Login-User-Budi-Kurniawan.`
15. Verifikasi tidak ada berkas terunduh pada Tab Changelog Detail
16. Lepas intercept (pulihkan response)
17. Pasang intercept yang memaksa respons 500 untuk request Download Borrowed Assets
18. Klik tab `Responsibilities`, sub-tab `Borrowed Assets`, lalu klik Download > `Download as CSV`
19. Verifikasi Toast error `Error, failed to download Borrowed-Assets-Budi-Kurniawan.`
20. Verifikasi tidak ada berkas terunduh pada Borrowed Assets
21. Lepas intercept (pulihkan response)
22. Pasang intercept yang memaksa respons 500 untuk request Download Assigned Assets
23. Klik sub-tab `Assigned Assets`, lalu klik Download > `Download as CSV`
24. Verifikasi Toast error `Error, failed to download Assigned-Assets-Budi-Kurniawan.`
25. Verifikasi tidak ada berkas terunduh pada Assigned Assets
26. Lepas intercept (pulihkan response)

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Kelas b (fault injection) ringan: intercept parsial di atas backend nyata; intercept dilepas pada langkah 5, 10, 16, 21, 26 (S-09).
- Langkah penghubung (S-03, R-16): langkah 1, 6, 12, 17, dan 22 (memasang intercept), langkah 11 (Search record yang dicari dan membuka Detail), langkah 5, 10, 16, 21, 26 (melepas intercept dan menutup modal).
- Asersi "tidak ada berkas terunduh" didahului Verifikasi toast error hasil server pada surface yang sama sebagai anchor (bagian 8b butir 2 dan 11).
- Temuan untuk QA:
  - TC-GS-NLU-498 memakai nama berkas `...-Budi-Kurniawan` pada toast Detail; spec membuka Detail record Pre-setup `Budi Kurniawan` (tanpa suffix) sehingga teks Expected TC diasersi apa adanya. Search `Budi Kurniawan` dapat memuat baris lain yang namanya memuat teks itu (record spec lain bersuffix); spec memilih baris dengan Name persis `Budi Kurniawan`.
  - TC-GS-NLU-298 dan 498 tidak menyebut cara mengamati "tidak ada berkas terunduh"; spec memakai pengamatan unduhan browser (kemampuan disediakan tim FE).
