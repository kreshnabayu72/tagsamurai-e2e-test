---
id: TC-FA-FAAC-E2E-181-defense-in-depth-request-langsung-tanpa-hak-update-403
title: "Defense-in-Depth: Request Langsung Assign, Move, Unassign, dan Cancel Scheduled Version Tanpa Hak Update Ditolak 403"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-618
  - TC-FA-FAAC-619
  - TC-FA-FAAC-620
  - TC-FA-FAAC-686
sourceRules: ["E-FAAC-78", "E-FAAC-82", "E-FAAC-110", "E-FAAC-114"]
smoke: []
dependsOn: []
trace:
  "E-FAAC-78": [2, 13, 16]
  "E-FAAC-82": [3, 11, 14, 17]
  "E-FAAC-110": 7
  "E-FAAC-114": [8, 10]
coverage:
  web: automated
---

# Defense-in-Depth: Request Langsung Assign, Move, Unassign, dan Cancel Scheduled Version Tanpa Hak Update Ditolak 403

## Prerequisites

- Mode: FE+BE
- Login akun aktor pertama (Read Only) dilakukan di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Role yang diuji (tiap role memakai akunnya sendiri):

| Role | Akun | Env var password | TC |
|---|---|---|---|
| Read Only | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_RO_PASSWORD` | TC-FA-FAAC-618, TC-FA-FAAC-686 |
| Create-Only | `createOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_CO_PASSWORD` | TC-FA-FAAC-619 |
| Delete-Only | `deleteOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_DO_PASSWORD` | TC-FA-FAAC-620 |

- Env var: `FA_AC_RO_PASSWORD`, `FA_AC_CO_PASSWORD`, `FA_AC_DO_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Kemampuan teknis: klien HTTP atau fixture BE yang mengirim request Assign, Move, Unassign, dan Cancel Scheduled Version langsung ke server tanpa melewati browser, memakai sesi API akun role yang bersangkutan (sesi API aktor, lihat suite.md; Create-Only dan Delete-Only tidak login lewat UI di spec ini); pembacaan keanggotaan Asset Name dan versi Scheduled lewat kemampuan baca BE. Seluruhnya disediakan tim FE/BE; endpoint dan bentuk request tidak didefinisikan di TC, PRD, atau LLD yang dibaca, sehingga tidak ditulis di spec.
- Data seed (kode dan nama literal TC, disediakan fixture BE, dibaca, tidak diubah karena semua request ditolak): Asset Class `Heavy Equipment` (`HEAVY-EQ`) Active; Asset Name tanpa Asset Class `Hand Truck`; Asset Name `Crane Rental Unit` ter-assign ke `Heavy Equipment`; Asset Class `Machinery` (`MACHINERY`) Active; Asset Class `B-SCHED` dengan versi Scheduled sejak M+2 (bulan berjalan M mengikuti zona waktu General Settings client, NC-11).
- Keadaan awal dinamis: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` (fixture BE menyetelnya sebelum TC-619 dan TC-620 dan memulihkan keadaan semula sesudahnya).
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (flag Guided Tooltip, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-618: Permintaan langsung Assign tanpa hak Update ditolak server dengan 403

1. Kirim permintaan Assign `Hand Truck` ke `HEAVY-EQ` sebagai Read Only langsung ke server tanpa melewati browser
2. Verifikasi respons server `403 Forbidden`
3. Verifikasi `Hand Truck` tetap tanpa Asset Class

### TC-FA-FAAC-686: Read Only tidak dapat Cancel Scheduled Version lewat permintaan langsung

4. Catat baseline lewat kemampuan baca BE: versi Scheduled `B-SCHED`
5. Ketik Search `B-SCHED`, tekan Enter
6. Klik link Class Code `B-SCHED` di tabel
7. Verifikasi Alert versi Scheduled tampil
8. Verifikasi tombol `[Cancel scheduled version]` pada Alert versi Scheduled Hidden
9. Kirim permintaan Cancel Scheduled Version atas `B-SCHED` sebagai Read Only langsung ke server tanpa melewati browser
10. Verifikasi respons server `403`
11. Verifikasi versi Scheduled `B-SCHED` tidak berubah

### TC-FA-FAAC-619: Permintaan langsung Move tanpa hak Update ditolak server dengan 403

12. Kirim permintaan Move `Crane Rental Unit` ke `MACHINERY` sebagai Create-Only langsung ke server tanpa melewati browser
13. Verifikasi respons server `403 Forbidden`
14. Verifikasi `Crane Rental Unit` tetap di `Heavy Equipment`

### TC-FA-FAAC-620: Permintaan langsung Unassign tanpa hak Update ditolak server dengan 403

15. Kirim permintaan Unassign `Crane Rental Unit` sebagai Delete-Only langsung ke server tanpa melewati browser
16. Verifikasi respons server `403 Forbidden`
17. Verifikasi `Crane Rental Unit` tetap ter-assign

## Notes

1. K-1: keempat TC adalah TC defense-in-depth kelas a dengan Expected berupa respons API (status respons dan state data lewat fixture BE). Tetap masuk spec FE+BE walau tumpang tindih dengan tc-[modul]-backend.md, karena TC granular tetap sumber dan tiap TC tepat satu spec; BE mencatatnya pada tingkat endpoint.
2. Sesuai bagian 8b butir 1, langkah request langsung hanya mengasersi respons server dan state data; tampilan tidak diasersi. Satu-satunya asersi UI adalah langkah 7 dan 8 (bagian pertama Expected TC-686 yang memang di UI).
3. Subjudul `###` memetakan langkah ke id TC granular. Urutan diubah dari urutan nomor: TC-686 (Read Only) diletakkan berdampingan dengan TC-618 karena akun aktor pertama Read Only; Create-Only dan Delete-Only hanya memakai sesi API akunnya sehingga tidak ada langkah ganti akun UI.
4. Spec Role Matrix negatif (bagian 3a) per aksi yang tidak berhak: tabel "Role yang diuji" berisi role yang tidak berhak atas aksinya; tiap role ditulis per blok TC karena aksinya berbeda per role.
5. Pembagian TC lintas spec (S-05): TC-618 dan TC-686 ada di spec ini (status respons 403, state data, dan UI) dan di spec 193; TC-619 dan TC-620 ada di spec ini dan di spec 194. Klausa "tidak ada entri log baru" (selisih jumlah entri Changelog Asset Class, System Log, dan Activity Log terhadap baseline, dengan permintaan yang sama sebagai pemicu) diasersi di spec 193 dan 194; spec ini tidak mengasersi log.
6. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 5 (Search untuk menemukan baris target, R-16).
7. Pengecualian kode dan nama seed literal (S-06/S-12): TC mewajibkan `HEAVY-EQ`, `MACHINERY`, `Hand Truck`, `Crane Rental Unit`, dan `B-SCHED`; dipakai apa adanya tanpa suffix `{runId}`. Semua permintaan ditolak sehingga data tidak berubah.
8. Temuan untuk QA: TC-618 sampai TC-620 tidak menyebut kode status selain `403 Forbidden`; TC-686 menyebut `403` saja. Spec mengikuti TC. Akun Create-Only dan Delete-Only dipakai lewat sesi API; TC menulis "sebagai Create-Only" tanpa menyebut cara login.
